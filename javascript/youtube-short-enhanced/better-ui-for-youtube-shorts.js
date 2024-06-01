/**
 * @file better-ui-for-youtube-shorts.js
 * @author Remco Stoeten (@remcostoeten on github)
 * @date 1 jun 2024
 *
 * This file contains the implementation for improving the UI for YouTube Shorts.
 * The main functionalities include:
 * 1. Functionality 1
*/

const BASE_URL = 'https://www.youtube.com';
const SHORTS_URL = `${BASE_URL}/shorts`;

const header = document.getElementById("masthead-container");
const navElements = document.querySelectorAll("[role='navigation']");

// Add transition CSS to smoothly animate the elements
header.style.transition = 'opacity 0.5s ease';
navElements.forEach(navElement => {
    navElement.style.transition = 'opacity 0.5s ease';
});
let isHidden = false;

function toggleUI() {
    if (window.location.href.includes(SHORTS_URL)) {
        if (isHidden) {
            header.style.opacity = '1';
            navElements.forEach(navElement => {
                navElement.style.opacity = '1';
            });
        } else {
            header.style.opacity = '0';
            navElements.forEach(navElement => {
                navElement.style.opacity = '0';
            });
        }
        isHidden = !isHidden;
    }
}

toggleUI();

// ToDo: add toggle btn