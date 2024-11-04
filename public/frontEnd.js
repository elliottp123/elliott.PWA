let result = "";

console.log("Starting fetch...");
fetch("http://localhost:5000/frontEndData.json")
  .then(function (response) {
    console.log("Response status:", response.status);
    return response.json();
  })
  .then(function (data) {
    console.log("Data received:", data);
    appendData(data);
  })
  .catch(function (err) {
    console.log("error: " + err);
  });

function appendData(data) {
  console.log("Starting to append data, length:", data.length);
  data.forEach(({ name, image, hyperlink, about, language } = rows) => {
    console.log("Processing:", name);
    result += `
        <div class="card">
        <img class="card-image" src="${image}" alt="Product image for the ${name} VSCode extension."/>
        <h1 class="card-name">${name}</h1>
        <p class="card-about">${about}</p>
        <a class="card-link" href="${hyperlink}"><button class="btn">Read More</button></a>
        </div>
        `;
  });
  console.log("Final HTML length:", result.length);
  document.querySelector(".container").innerHTML = result;
}
