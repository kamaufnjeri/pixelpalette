/*
Document event listener for DOMContentLoaded
*/
document.addEventListener("DOMContentLoaded", function () {
  // Get elements from the DOM
  const artworkIndicators = document.getElementById('artwork-indicators');
  const exhibits = document.getElementById('exhibits');

  /*
  Function to calculate time difference between current date and target date
  */
  function getTimeDifference(startDate) {
    const currentDate = new Date().getTime();
    const targetDate = new Date(startDate).getTime();
    const timeDifference = targetDate - currentDate;
    const timeRemaining = {};

    timeRemaining.days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    timeRemaining.hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    timeRemaining.minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    timeRemaining.seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    return timeRemaining;
  }

  // Check if exhibits element exists
  if (exhibits) {
    const exhibitsList = exhibits.querySelectorAll('.exhibit');
    exhibitsList.forEach((exhibit) => {
      // Get the start date attribute from the exhibit
      const startDate = exhibit.getAttribute('data-start-date');
      const timeRemaining = getTimeDifference(startDate, exhibit);

      // Hide exhibit button if the exhibition has started
      if (
        timeRemaining.days >= 0 &&
        timeRemaining.hours >= 0 &&
        timeRemaining.minutes >= 0 &&
        timeRemaining.seconds > 0
      ) {
        exhibit.querySelector('.exhibit-btn').style.display = 'None';
      }

      // Update the time remaining every second
      setInterval(function () {
        const timeRemaining = getTimeDifference(startDate, exhibit);

        // Display time remaining if the exhibition has not ended
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
          // Clear time display and show exhibit button if exhibition has ended
          exhibit.querySelector('.days').innerHTML = '';
          exhibit.querySelector('.hours').innerHTML = '';
          exhibit.querySelector('.minutes').innerHTML = '';
          exhibit.querySelector('.seconds').innerHTML = '';
          exhibit.querySelector('.exhibit-btn').style.display = 'flex';
        }

      }, 1000);
    });
  }

  // Check if artwork indicators element exists
  if (artworkIndicators) {
    const indicators = artworkIndicators.querySelectorAll('.indicator');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const slider = document.querySelector('.slides');
    let currentIndex = 0;
    let intervalId;

    // Set the first indicator as active on window load
    window.onload = function () {
      indicators[0].classList.add('active');
    };

    // Event listener for the next button
    nextButton.addEventListener('click', () => {
      transitionTo(currentIndex + 1);
    });

    // Event listener for the previous button
    prevButton.addEventListener('click', () => {
      transitionTo(currentIndex - 1);
    });

    // Event listener for each indicator
    indicators.forEach((indicator, index) => {
      indicator.addEventListener('click', () => {
        transitionTo(index);
      });
    });

    /*
    Function to transition to the specified index
    */
    function transitionTo(index) {
      currentIndex = index;

      // Ensure index is within the valid range
      if (currentIndex < 0) {
        currentIndex = indicators.length - 1;
      } else if (currentIndex >= indicators.length) {
        currentIndex = 0;
      }

      // Calculate the left value for the slider
      const leftValue = -currentIndex * 800;
      slider.style.left = leftValue + 'px';
      stopInterval();
      startInterval();
      updateIndicators();
    }

    /*
    Function to update the active indicator
    */
    function updateIndicators() {
      indicators.forEach((indicator, index) => {
        indicator.classList.remove('active');
        if (index === currentIndex) {
          indicator.classList.add('active');
        }
      });
    }

    /*
    Function to start the interval for automatic transitions
    */
    function startInterval() {
      stopInterval();
      intervalId = setInterval(() => {
        transitionTo(currentIndex + 1);
      }, 4000);
    }

    /*
    Function to stop the automatic transition interval
    */
    function stopInterval() {
      clearInterval(intervalId);
    }

    // Start the interval on window load
    startInterval();
  }
});
