var fileBool = false;
var themeBool = false;
var acceptedFileTypes = [
    "application/doc",
    "application/ms-doc",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
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
        console.log("Must be .doc or .docx");
      }
    } else {
      console.log("Only drop a single file");
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
    thumbnailElement = document.createElement("div");
    thumbnailElement.classList.add("drop-zone__thumb");
    dropZoneElement.appendChild(thumbnailElement);
  }

  thumbnailElement.dataset.label = file.name;
}
