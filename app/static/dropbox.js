const dropbox = document.getElementById("dropbox");
const fileInput = document.getElementById("fileInput");
const loader = document.getElementById("loader");
const resultbox = document.getElementById("result");

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
        <img class="max-h-40 max-w-100" src="${URL.createObjectURL(
          files[0]
        )}" alt="your image" />
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
  resultbox.innerHTML =
    '<p class="text-gray-600">Upload an image to see the result.</p>';
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      hideLoader();
      colors = data.data;
      resultbox.innerHTML = `
          <p class="mb-4">These are the main colors present in the image with total occupancy percentage.</p>
          <ul class="space-y-4">
              ${colors
                .map(
                  (color) => `
                  <li class="flex items-center p-4 bg-gray-150 border border-gray-200 rounded-md">
                      <div class="w-10 h-10 rounded-md mr-4 flex-shrink-0 border border-gray-300" style="background-color: ${color.hex_code};"></div>
                      <div>
                          <span class="text-lg capitalize font-semibold text-gray-800">
                              ${color.color_name}
                          </span>
                          <div class="text-sm text-gray-600">rgb(${color.red}, ${color.green}, ${color.blue})</div>
                          <div class="text-sm text-gray-600">${color.hex_code}</div>
                          <div class="text-sm text-gray-600 mt-1">${color.percentage}%</div>
                      </div>
                  </li>
              `
                )
                .join("")}
          </ul>
      `;
    })
    .catch((error) => {
      hideLoader();
      resultbox.innerHTML = `
          <p class="text-red-600">An error occurred while processing the image. Please try again.</p>
      `;
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
