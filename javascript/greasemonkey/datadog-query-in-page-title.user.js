// ==UserScript==
// @name        datadoghq.eu/logs - add query in title
// @namespace   Violentmonkey Scripts
// @match       https://lumapps.datadoghq.eu/logs*
// @grant       none
// @version     1.0
// @author      -
// @description 02/07/2024 11:51:06
// ==/UserScript==

window.setInterval(function() {
  let params = new URL(document.location).searchParams;
  let query = params.get("query");
  document.title = `${query} - Datadog logs`;
}, 1000);
