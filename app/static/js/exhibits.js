document.addEventListener("DOMContentLoaded", function () {
 
  const artworkIndicators = document.getElementById('artwork-indicators');
  

  const exhibits = document.getElementById('exhibits');
  if (exhibits) {
    const exhibitsList = exhibits.querySelectorAll('.exhibit');
    exhibitsList.forEach(exhibit => {
      startDate = exhibit.getAttribute('data-start-date');
      currentDate = new Date().getTime();
      targetDate = new Date(startDate).getTime();
      timeDifference = targetDate - currentDate;
      let days = Math.floor(timeDifference / (1000*60*60*24));
      let hours = Math.floor(timeDifference % (1000*60*60*24) / (1000*60*60));
      let minutes = Math.floor(timeDifference % (1000*60*60) / (1000*60));
      let seconds = Math.floor(timeDifference % (1000*60) / 1000);
      console.log(days);
      console.log(hours);
      console.log(minutes);
      console.log(seconds);
      
      if (timeDifference > 0) {
        document.getElementById('days').innerHTML = (days < 10) ? '0' + days : days + 'days';
        document.getElementById('hours').innerHTML = (hours < 10) ? '0' + hours : hours + 'hours';
        document.getElementById('minutes').innerHTML = (minutes < 10) ? '0' + minutes : minutes + 'minutes';
        document.getElementById('seconds').innerHTML = (seconds < 10) ? '0' + seconds : seconds + 'seconds';
      }
    })
  }

  if (artworkIndicators) {
    const indicators = artworkIndicators.querySelectorAll('.indicator');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const slider = document.querySelector('.slides');
    let currentIndex = 0;
  let intervalId;

  window.onload = function () {
    indicators[0].classList.add('active');
  }
  nextButton.addEventListener('click', () => {
    console.log(nextButton);
      transitionTo(currentIndex + 1);
  });
  prevButton.addEventListener('click', () => {
    console.log(prevButton);
    transitionTo(currentIndex - 1);
});

indicators.forEach((indicator, index) => {
  indicator.addEventListener('click', () => {
      transitionTo(index);
  });
});


function transitionTo(index) {
  currentIndex = index;
  if (currentIndex < 0) {
      currentIndex = indicators.length - 1;
  } else if (currentIndex >= indicators.length) {
      currentIndex = 0;
  }

  const leftValue = -currentIndex * 800;
  slider.style.left = leftValue + 'px';
  stopInterval();
  startInterval();
  updateIndicators();
}
function updateIndicators() {
  indicators.forEach((indicator, index) => {
      indicator.classList.remove('active');
      if (index === currentIndex) {
          indicator.classList.add('active');
      }
  });
}
function startInterval() {
  stopInterval();
  intervalId = setInterval(() => {
      transitionTo(currentIndex + 1);
  }, 4000);
}

    function stopInterval() {
      clearInterval(intervalId);
}


    startInterval();
    console.log(prevButton)
// console.log(nextButton)
  }
});