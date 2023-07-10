/*
 * All code here should run at startup of the base.html template
 * */

// Handling active class on Grupo links

// get all menu items

function addMenuEventListeners() {

    var menuInnerItems = document.querySelectorAll('.menu-inner > .menu-item');

    // add click event listener to all menu inner items
    menuInnerItems.forEach(item => {
        item.addEventListener('click', function(event) {
            // prevent default link behavior
            event.preventDefault();

            // remove active class from all menu inner items
            menuInnerItems.forEach(i => i.classList.remove('active'));

            // add active class to the clicked menu inner item
            this.classList.add('active');

            // clear all menu sub item
            var menuSubItems = document.querySelectorAll('.menu-sub .active');
            menuSubItems.forEach(subitem => {
                subitem.classList.remove('active')
            });
        });
    });

    // Handling active class on Macroprocesso links

    // get all menu items
    var menuSubItems = document.querySelectorAll('.menu-sub > .menu-item');

    // add click event listener to all menu sub items
    menuSubItems.forEach(item => {
        item.addEventListener('click', function(event) {
            // prevent default link behavior
            event.preventDefault();

            // prevent propagation
            event.stopPropagation();

            // remove active class from all menu sub items
            menuSubItems.forEach(i => i.classList.remove('active'));

            // add active class to the clicked menu sub item
            this.classList.add('active');
        });
    });


    // Handling open class on Grupo links

    // get all Grupo with Macro
    var grupoWithMacro = document.querySelectorAll('.menu-link.menu-toggle');

    //
    grupoWithMacro.forEach(function(element) {
        element.addEventListener('click', function(event) {
            event.preventDefault();
            this.parentNode.classList.toggle('open');
        });
    });
}
