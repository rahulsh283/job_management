$(document).ready(function(){

    $("#country_id").on('change', function(){
      
      var country_id = $(this).val();
      $.ajax({
        url : '/state-list-by-country/'+country_id,
        type: 'GET',
        dataType: 'json',
        data : {},
        success: function(data){

          console.log(data);
          var option_list = '';
          if(data.error == 0){

            var state_list = data.state_list;
            $.each(state_list, function(k, v){
              option_list += '<option value="'+v.id+'">'+v.name+'</option>';
            });
          }
          $('#state_id').html(option_list);
        }
      });
    });

    // update resume for user
    $("#update_resume_data").validate({
        rules:{
            user_resume : {
                required: true,
            }
        },
        submitHandler: function(form){
            var formData = new FormData($("#update_resume_data")[0]);
    
            $.ajax({
    
              url : "/update-user-resume",
              type : "POST",
              dataType: "json",
              data : formData,
              cache: false,
              contentType: false,
              processData: false,
              success : function(newdata){
    
                alert(newdata.msg);
                if(newdata.error == 0){
                    
                    let file_name = newdata.file_name
                    let file_path = file_name;
                    $('#user_updated_resume').attr('href', file_path);
                }
                
              }
            });
        }
    });

    // update user Details
    $("#update_user_form").validate({
      rules:{
          first_name : {
              required: true,
          }
      },
      submitHandler: function(form){
  
          $.ajax({
  
            url : "/update-user-deatil",
            type : "POST",
            dataType: "json",
            data : $("#update_user_form").serialize(),
            success : function(newdata){
  
              alert(newdata.msg);
              if(newdata.error == 0){
                  
                  location.reload();
              }
              
            }
          });
      }
  });
});