document.addEventListener('DOMContentLoaded', function() {
    setTimeout(displaySuccess, 750);
});

function displaySuccess() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("success").style.display = "block";
    document.getElementById("downloadBtn").style.display = "inline";
    document.getElementById("pptx-status").innerHTML = "All done, click below to get your powerpoint!"
}
