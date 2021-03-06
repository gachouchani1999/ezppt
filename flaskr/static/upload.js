var fileBool = false;
var themeBool = false;
var acceptedFileTypes = [
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
]

function updateGenerateBtn() {
    console.log(!(fileBool && themeBool));
    document.getElementById("generateSlidesBtn").disabled = !(fileBool && themeBool);
}

function themeClickHandler() {
    document.querySelectorAll('.td')
    .forEach(e => e.style.border = "none");
    this.style.border = "2px solid #337ab7";
    document.getElementById("theme").value = this.dataset.themeNum;
    themeBool = true; updateGenerateBtn();
}

document.querySelectorAll('.td')
.forEach(e => e.addEventListener("click", themeClickHandler));

// Modifies https://codepen.io/dcode-software/pen/xxwpLQo
document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
  const dropZoneElement = inputElement.closest(".drop-zone");

  dropZoneElement.addEventListener("click", (e) => {
    inputElement.click();
  });

  inputElement.addEventListener("change", (e) => {
    if (inputElement.files.length == 1) {
      updateThumbnail(dropZoneElement, inputElement.files[0]);
      fileBool = true; updateGenerateBtn();
    }
  });

  dropZoneElement.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZoneElement.classList.add("drop-zone--over");
  });

  ["dragleave", "dragend"].forEach((type) => {
    dropZoneElement.addEventListener(type, (e) => {
      dropZoneElement.classList.remove("drop-zone--over");
    });
  });

  dropZoneElement.addEventListener("drop", (e) => {
    e.preventDefault();

    if (e.dataTransfer.files.length == 1) {
      file = e.dataTransfer.files[0];
      if (acceptedFileTypes.includes(file.type)) {
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(dropZoneElement, file);
        fileBool = true; updateGenerateBtn();
      } else {
        alert("Please upload a .docx extension");
      }
    } else {
      alert("Please upload a single file");
    }

    dropZoneElement.classList.remove("drop-zone--over");
  });
});

/**
 * Updates the thumbnail on a drop zone element.
 *
 * @param {HTMLElement} dropZoneElement
 * @param {File} file
 */
function updateThumbnail(dropZoneElement, file) {
  let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

  // First time - remove the prompt
  if (dropZoneElement.querySelector(".drop-zone__prompt")) {
    dropZoneElement.querySelector(".drop-zone__prompt").remove();
  }

  // First time - there is no thumbnail element, so lets create it
  if (!thumbnailElement) {
    thumbnailDiv = document.createElement("div");
    thumbnailDiv.setAttribute('class','drop-zone__thumb');
    thumbnailImage = document.createElement("img");
    thumbnailImage.src = "/static/media/file.png";
    thumbnailDiv.appendChild(thumbnailImage);
    thumbnailText = document.createElement("p");
    thumbnailText.setAttribute('id','thumbnail-text');
    thumbnailDiv.appendChild(thumbnailText);
    dropZoneElement.appendChild(thumbnailDiv);
  }

  document.getElementById('thumbnail-text').innerHTML = file.name;
}
