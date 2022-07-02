// ==UserScript==
// @name        reddit.com - hide some users
// @namespace   Violentmonkey Scripts
// @match       https://www.reddit.com/r/*/
// @grant       GM_getValue
// @version     1.0
// @author      hydrargyrum
// @description 09/01/2022, 19:54:10
// ==/UserScript==

var users = GM_getValue("users", []);

var users_re = new RegExp(users.join("|"));

let timerId = window.setInterval(
  () => {
    let links = document.querySelectorAll('a[href^="/user/"]');

    for (let link of links) {
      if (link.href.match(users_re)) {
        let parent = link.parentNode;

        while (parent.parentNode) {
          let attr = parent.attributes["data-testid"];

          if (attr && attr.value == "post-container") {
            parent.parentNode.removeChild(parent);
            break;
          }
          parent = parent.parentNode;
        }
      }
    }
  }, 2000
);
