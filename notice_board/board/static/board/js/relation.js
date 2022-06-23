var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

relationManager = {
    init: function () {

        $( document ).ready(function() {
          console.log('init actions')
        this.hide_buttons = $('[action="hide"]');
        this.add_to_favorites_buttons = $('[action="favorite"]')

        this.hide_buttons.on('click', this.on_click);
        this.add_to_favorites_buttons.on('click', this.on_click);
        }.bind(this));
    },

    on_click(event) {
        var method = '';
        if (event.target.attributes.action.value == 'favorite') {
            $(event.target).addClass('has-text-danger');
            method = 'favorite';
        }
        if (event.target.attributes.action.value == 'hide') {
            $(event.target).parent().parent().parent().hide('slow')
            method = 'hide';
        }
        $.ajax({
            url: '/relation',
            type : 'POST',
            contentType : 'application/json',
            data: JSON.stringify({
                method: method,
                pk: event.target.attributes.data.value,

            })
        }).done(function () {
            console.log('done')
        });
    }
}
relationManager.init()

// <i className="fa-solid fa-eye-slash icon-medium" action="hide"></i>
// <i className="fa-solid fa-star icon-medium" action="add_to_favorites"></i>