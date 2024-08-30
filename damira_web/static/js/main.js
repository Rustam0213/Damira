document.addEventListener('DOMContentLoaded', function() {
  const hamburger = document.querySelector('.hamburger');
  const sidebar = document.getElementById('sidebar');
  const closebtn = document.getElementById('closebtn');
  
  if (hamburger && sidebar && closebtn) {
    hamburger.addEventListener('click', function() {
      this.classList.toggle('open');
      sidebar.classList.toggle('open');
    });

    closebtn.addEventListener('click', function() {
      hamburger.classList.remove('open');
      sidebar.classList.remove('open');
    });
  } else {
    console.error('Element(s) not found.');
  }
});

document.addEventListener('DOMContentLoaded', function() {
  const consentCookieName = 'cookie_consent';
  const consentCookieValueAccepted = 'accepted';
  const consentCookieValueRejected = 'rejected';
  const consentElement = document.getElementById('cookie-consent');
  const acceptButton = document.getElementById('accept-cookies');
  const rejectButton = document.getElementById('reject-cookies');

  // Проверяем, есть ли уже cookie согласия
  if (!getCookie(consentCookieName)) {
      consentElement.style.display = 'block';
  }

  // Устанавливаем cookie и скрываем окно при принятии
  acceptButton.addEventListener('click', function() {
      setCookie(consentCookieName, consentCookieValueAccepted, 365);
      consentElement.style.display = 'none';
  });

  // Устанавливаем cookie и скрываем окно при отказе
  rejectButton.addEventListener('click', function() {
      setCookie(consentCookieName, consentCookieValueRejected, 365);
      consentElement.style.display = 'none';
  });

  // Функция для получения cookie по имени
  function getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
  }

  // Функция для установки cookie
  function setCookie(name, value, days) {
      let expires = '';
      if (days) {
          const date = new Date();
          date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
          expires = `; expires=${date.toUTCString()}`;
      }
      document.cookie = `${name}=${value || ''}${expires}; path=/`;
  }
});
