const menuButton = document.querySelector("#menu-button");
const menu = document.querySelector("#menu");
const toggler = document.querySelector("#toggler");
const html = document.querySelector("html");

getThemeColorOnRefresh = () => {
    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'dark') {
            html.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            html.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }
    } else {
        // if NOT set via local storage previously set dark as default
        localStorage.setItem('color-theme', 'light');
    }
}

toggleDarkMode = () => {
    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            html.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            html.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }
    } else {
        // if NOT set via local storage previously
        if (html.classList.contains('dark')) {
            html.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            html.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
}

menuButton.addEventListener('click', () => menu.classList.toggle("hidden"));
toggler.addEventListener('click', () => toggleDarkMode());

getThemeColorOnRefresh();

// ----------------------- Single Page functionality ----------------------- 
const activeListing = document.querySelector("#active-listing");
const activeListingBtn = document.querySelector("#active-listing-btn");
const watchlist = document.querySelector("#watchlist");
const watchlistBtn = document.querySelector("#watchlist-btn");
const item = document.querySelector("#item");
const itemBtns = document.querySelectorAll(".item-btn");
const createListing = document.querySelector("#create-listing");
const createListingBtn = document.querySelector("#create-listing-btn");
const login = document.querySelector("#login");
const loginBtn = document.querySelector("#login-btn");
const register = document.querySelector("#register");
const registerBtn = document.querySelector("#register-btn");


activeListingBtn.addEventListener('click', () => {
    watchlist.classList.add("hidden");
    item.classList.add("hidden");
    createListing.classList.add("hidden");
    login.classList.add("hidden");
    register.classList.add("hidden");

    activeListing.classList.remove("hidden");
});

watchlistBtn.addEventListener('click', () => {
    console.log("watchlist");
    activeListing.classList.add("hidden");
    item.classList.add("hidden");
    createListing.classList.add("hidden");
    login.classList.add("hidden");
    register.classList.add("hidden");

    watchlist.classList.remove("hidden");
});

itemBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        console.log("item");
        activeListing.classList.add("hidden");
        watchlist.classList.add("hidden");
        createListing.classList.add("hidden");
        login.classList.add("hidden");
        register.classList.add("hidden");

        item.classList.add("flex");
        item.classList.remove("hidden");
    });
});

createListingBtn.addEventListener('click', () => {
    console.log("create listing");
    activeListing.classList.add("hidden");
    watchlist.classList.add("hidden");
    item.classList.add("hidden");
    login.classList.add("hidden");
    register.classList.add("hidden");

    createListing.classList.remove("hidden");
});

loginBtn.addEventListener('click', () => {
    console.log("login");
    activeListing.classList.add("hidden");
    watchlist.classList.add("hidden");
    item.classList.add("hidden");
    createListing.classList.add("hidden");
    register.classList.add("hidden");

    login.classList.remove("hidden");
});

registerBtn.addEventListener('click', () => {
    console.log("register");
    activeListing.classList.add("hidden");
    watchlist.classList.add("hidden");
    item.classList.add("hidden");
    createListing.classList.add("hidden");
    login.classList.add("hidden");

    register.classList.remove("hidden");
});
