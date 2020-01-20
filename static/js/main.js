function toggleMenu() {
    var navbar = document.getElementById("navbar-burger");
    navbar.classList.toggle("is-active");

    var navbarMenu = document.getElementById("navbar");
    navbarMenu.classList.toggle("is-active");
}

document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        $notification = $delete.parentNode;

        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });
    });
});