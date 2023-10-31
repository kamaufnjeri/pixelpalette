document.addEventListener("DOMContentLoaded", function () {
  const artworkIndicators = document.getElementById('artwork-indicators');
  const exhibits = document.getElementById('exhibits');

  function getTimeDifference(startDate) {
    const currentDate = new Date().getTime();
    const targetDate = new Date(startDate).getTime();
    const timeDifference = targetDate - currentDate;
    const timeRemaining = {};

    timeRemaining.days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    timeRemaining.hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    timeRemaining.minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    timeRemaining.seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    return timeRemaining
  }

  if (exhibits) {
    const exhibitsList = exhibits.querySelectorAll('.exhibit');
    exhibitsList.forEach((exhibit) => {
      const startDate = exhibit.getAttribute('data-start-date');
      const timeRemaining = getTimeDifference(startDate, exhibit);
      if (
        timeRemaining.days >= 0 &&
        timeRemaining.hours >= 0 &&
        timeRemaining.minutes >= 0 &&
        timeRemaining.seconds > 0
      ) {
        exhibit.querySelector('.exhibit-btn').style.display = 'None';
      }

      setInterval(function () {
        const timeRemaining = getTimeDifference(startDate, exhibit);
        if (
          timeRemaining.days >= 0 &&
          timeRemaining.hours >= 0 &&
          timeRemaining.minutes >= 0 &&
          timeRemaining.seconds >= 0
        ) {
          const days = timeRemaining.days < 10 ? '0' + timeRemaining.days : timeRemaining.days;
          const hours = timeRemaining.hours < 10 ? '0' + timeRemaining.hours : timeRemaining.hours;
          const minutes = timeRemaining.minutes < 10 ? '0' + timeRemaining.minutes : timeRemaining.minutes;
          const seconds = timeRemaining.seconds < 10 ? '0' + timeRemaining.seconds : timeRemaining.seconds;
          exhibit.querySelector('.days').innerHTML = 'Exhibit in ' + days + ' days';
          exhibit.querySelector('.hours').innerHTML = hours + ' hours';
          exhibit.querySelector('.minutes').innerHTML = minutes + ' minutes';
          exhibit.querySelector('.seconds').innerHTML = seconds + ' seconds';
          exhibit.querySelector('.exhibit-btn').style.display = 'None';
        } else if (
          timeRemaining.days <= 0 &&
          timeRemaining.hours <= 0 &&
          timeRemaining.minutes <= 0 &&
          timeRemaining.seconds < 0
        ) {
          exhibit.querySelector('.days').innerHTML = '';
          exhibit.querySelector('.hours').innerHTML = '';
          exhibit.querySelector('.minutes').innerHTML = '';
          exhibit.querySelector('.seconds').innerHTML = '';
          exhibit.querySelector('.exhibit-btn').style.display = 'flex';
        }

    }, 1000);
  });
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
    };

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
  }
});
