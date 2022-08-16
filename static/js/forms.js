$(document).ready(function () {
    /*
    Starts the autocomplete method with the database titles the view provides.
    It starts from when a user types 1 character with a delay of 100ms.
    autoFocus is used to automatically select the first result from the list.
    */
    $("#job-title").autocomplete({
        source: autocomplete_title_source,
        minLength: 1,
        delay: 100,
        autoFocus: true,
    });
})