const dropbox = document.getElementById("dropbox");
const fileInput = document.getElementById("fileInput");

// Trigger file input when dropbox is clicked
dropbox.addEventListener("click", () => {
  fileInput.click();
});

// Handle file drop
dropbox.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropbox.classList.add("bg-gray-200");
});

dropbox.addEventListener("dragleave", () => {
  dropbox.classList.remove("bg-gray-200");
});

dropbox.addEventListener("drop", (event) => {
  event.preventDefault();
  dropbox.classList.remove("bg-gray-200");
  const files = event.dataTransfer.files;
  handleFiles(files);
});

// Handle file selection through file input
fileInput.addEventListener("change", (event) => {
  const files = event.target.files;
  handleFiles(files);
});

function handleFiles(files) {
  if (files.length > 0) {
    dropbox.innerHTML = `<p class="text-gray-800">${files[0].name}</p>`;
  }
}

document.getElementById("uploadButton").addEventListener("click", () => {
  alert("File uploaded successfully!");
});
