from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        # userDetails = ['user_detail']
        # print(userDetails)
        current_path = request.path
        withoutLoginPath = ['/login', '/registration']
        loginPath = ['/user/profile', '/user']
       
        if 'user_detail' in request.session and current_path in withoutLoginPath:
            
            return redirect('/user')
        elif 'user_detail' not in request.session and current_path in loginPath:

            return redirect('/login')
        else:

            response = get_response(request)
            return response

    return middleware