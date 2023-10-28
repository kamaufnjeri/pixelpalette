// script.js
const exhibits = exhibits = [
  {
      title: "Exhibit 1",
      description: "Description for Exhibit 1",
      image_url: "image1.jpg",
      price: "Ksh 100",
      running_time: "2 hours",
  },
  {
      title: "Exhibit 2",
      description: "Description for Exhibit 2",
      image_url: "image2.jpg",
      price: "Ksh 75",
      running_time: "1.5 hours",
  },
    ];

const exhibitsContainer = document.querySelector('.exhibits-container');

exhibits.forEach(exhibit => {
  const exhibitItem = document.createElement('div');
  exhibitItem.classList.add('exhibit');

  exhibitItem.innerHTML = `
      <h2>${exhibit.title}</h2>
      <img src="${exhibit.image_url}" alt="${exhibit.title}">
      <p>${exhibit.description}</p>
      <p>${exhibit.price}</p>
      <p>Running Time: ${exhibit.running_time}</p>
  `;

  exhibitsContainer.appendChild(exhibitItem);
});
