const dropbox = document.getElementById("dropbox");
const fileInput = document.getElementById("fileInput");
const loader = document.getElementById("loader");

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
    dropbox.innerHTML = `<p class="text-gray-800">
        <img class="max-h-40 max-w-100" src="${URL.createObjectURL(files[0])}" alt="your image" />
    </p>`;
  }
}

document.getElementById("uploadButton").addEventListener("click", () => {
  const error = document.getElementById("error");
  if (!fileInput.files[0]) {
    error.innerHTML = "Please select an image of the file to upload.";
    return;
  } else {
    error.innerHTML = "";
  }

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);
  showLoader();
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
        hideLoader();
      console.log(data);
    });
});

function hideLoader() {
    loader.classList.add("hidden");
    loader.classList.remove("flex");
}

function showLoader() {
    loader.classList.remove("hidden");
    loader.classList.add("flex");
}