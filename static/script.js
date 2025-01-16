document.getElementById("downloadForm").addEventListener("submit", function (event) {
    const urlInput = document.getElementById("url").value.trim();
    if (!urlInput) {
        event.preventDefault();
        alert("Please enter a valid YouTube URL!");
    }
});
