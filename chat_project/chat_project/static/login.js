$(document).ready(function() {
  $('.login-form').on('click', function() {
    var $this = $(this);
    $this.button('loading')
    setTimeout(function(){
      $.ajax({
        beforeSend: function(msg){
          $this.button('loading')
        },
        type:"POST",
        url: $('form[name="login_form"]').attr('action'),
        data: $('form[name="login_form"]').serialize(),
        // the success function is called in the case of an http 200 response
        success: function(response){
            $this.button('reset');
            window.localStorage.setItem('x-access-token', response.token);
            window.location = "{% url 'home'  %}";
        },
        error: function(xhr, ajaxOptions, thrownError){
            alert('login failed - please try again');
            $this.button('reset');
        },
      });
      console.log("complete");
    }, 1000);
  });
});
