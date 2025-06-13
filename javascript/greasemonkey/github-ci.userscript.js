// ==UserScript==
// @name        github.com - notify when all CI checks on open PR are finished
// @namespace   Violentmonkey Scripts
// @match       https://github.com/*/*/pull/*
// @grant       GM_notification
// @version     1.0
// @author      hydrargyrum
// @description 08/06/2025 13:59:54
// ==/UserScript==

let inprogress = false;

let ciInterval = window.setInterval(function() {
  for (let el of document.querySelectorAll("h3")) {
    if (el.textContent == "Some checks haven't completed yet") {
      inprogress = true;
      break;
    } else if (el.textContent == "All checks have passed") {
      if (inprogress) {
        GM_notification(
          `CI succeeded at ${document.location} ✅\n\n${document.title}`,
          "Github CI",
          "https://github.githubassets.com/favicons/favicon-success.png"
        );
      }
      window.clearInterval(ciInterval);
      break;
    } else if (el.textContent == "Some checks were not successful") {
      if (inprogress) {
        GM_notification(
          `CI failed at ${document.location} ❌\n\n${document.title}`,
          "Github CI",
          "https://github.githubassets.com/favicons/favicon-failure.png"
        );
      }
      window.clearInterval(ciInterval);
      break;
    }
  }
}, 1000);
