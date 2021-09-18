document.addEventListener('DOMContentLoaded', function() {
    setTimeout(changeDisplay, 5000);
});

function changeDisplay() {
    if (Math.random() > 0.5) {
        displaySuccess()
    } else {
        displayFailure()
    }
}

function displaySuccess() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("success").style.display = "block";
    document.getElementById("downloadBtn").style.display = "inline";
    document.getElementById("pptx-status").innerHTML = "All done, click below to get your powerpoint!"
}

function displayFailure() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("failure").style.display = "block";
    document.getElementById("restartBtn").style.display = "inline";
    document.getElementById("pptx-status").innerHTML = "Hmm, looks like something went wrong..."
}
