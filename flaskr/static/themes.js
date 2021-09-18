function clickHandler() {
    document.querySelectorAll('.themes-table td')
    .forEach(e => e.style.border = "none");
    this.style.border = "2px solid #337ab7";
    document.getElementById("theme").value = this.dataset.themeNum;
}

document.querySelectorAll('.themes-table td')
.forEach(e => e.addEventListener("click", clickHandler));
