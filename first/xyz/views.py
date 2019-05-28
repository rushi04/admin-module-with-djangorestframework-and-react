from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
import jwt,json
from first import settings
from rest_framework import views, filters
from django.http import HttpResponse, HttpRequest
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .api_serializer import UserSerailizer, AccountSerializer, AdminSerializer
from .models import UsersTbl, UserAccountDetailTbl, AdminUsersTbl, WalletWithdrawalRequestTbl, UserWalletInfoTbl, UserPanDetailTbl, UserTransactionHistory, AdminCommentsTbl
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db.models import Avg, Count, Min, Sum

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )

from rest_framework_word_filter import FullWordSearchFilter

from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

# Create your views here.

#creating an api for fetching the past transactions of the user
#first create a class based view
#make a get function to handle the get request_date
#

class ViewSet(ObjectMultipleModelAPIViewSet):  #the ObjectMultipleModelAPIViewSet is used for multiple models based api.
    #permission_classes = (IsAuthenticated,)
    querylist=(
        {'queryset':UsersTbl.objects.all(),'serializer_class':UserSerailizer},
        {'queryset':UserAccountDetailTbl.objects.all(),'serializer_class':AccountSerializer}
    )
    filter_backends = (FullWordSearchFilter,)
    word_fields = ('user_id',)

def users_detail(request,id):

    #in the request block we get authorization token which we check to authenticate the request.
    auth = get_authorization_header(request).split()

    # learn more about getting headers and working on them.

    try:
        token = auth[1]
        if token=="null":
            msg = 'Null token not allowed'
            raise exceptions.AuthenticationFailed(msg)
    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        raise exceptions.AuthenticationFailed(msg)


    model = AdminUsersTbl
    payload = jwt.decode(token, settings.SECRET_KEY)

    # print( "payload", payload)

    id1 = payload['login']['id']
    msg = {'Error': "Token mismatch",'status' :"401"}
    error_not_found = {'Error': "No User Found",'status' :"404"}


    print(id1)

# AUTHENTICATING:
    try:
        user1 = AdminUsersTbl.objects.get(
            id=id1,
        )

        #if not user.token['token'] == token:
        if not user1:
            raise exceptions.AuthenticationFailed(msg)
    except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
        return HttpResponse({'Error': "Token is invalid"}, status="403")
    except User.DoesNotExist:
        return HttpResponse({'Error': "Internal server error"}, status="500")

# AUTHERIZING:
    print(0)
    try:

            user = UsersTbl.objects.get(user_email=id)
    except:
        try:
            id = int(id)
            user = UsersTbl.objects.get(user_id=id)
        except:
            try:
                    user = UsersTbl.objects.get(user_mobile=id)
            except:
                    return JsonResponse(error_not_found)


    #make use of serializers, it will make the code extremely short and organisedself.
    id = user.user_id
    personal_details = {
            "user_name":user.user_name,
            "user_id":user.user_id,
            "user_dob":user.user_dob,
            "first_name":user.first_name,
            "user_profile_pic":user.user_profile_pic,
            "last_name":user.last_name,
            "is_mob_num_verified":user.is_mob_num_verified,
            "is_email_verified":user.is_email_verified,
            "user_email":user.user_email,
        }

    if UserAccountDetailTbl.objects.filter(user_id=id):
        user1 = UserAccountDetailTbl.objects.get(user_id=id)
        account_details={
            "added":1,
            "bank_acc_no":user1.bank_acc_no,
            "acc_holder_name":user1.acc_holder_name,
            "is_verified":user1.is_verified,
            "bank_name":user1.bank_name,
        }
    else:
        account_details={"added":0}

#the below code is for giving the total amount withdrawn by the user_referral_tbl
#we will be using the sum aggregator from django ormself.

    if UserWalletInfoTbl.objects.filter(user_id=id):
        user2 = UserWalletInfoTbl.objects.get(user_id=id)
        user2.__dict__
        total_balance_amount = {
            "balance_available":1,
            "total_balance_amount":user2.total_balance,
        }
    else:
        total_balance_amount = {
            "balance_available":0,
        }
# the following code is for fetching the total balance of the user_referral_tbl
    if WalletWithdrawalRequestTbl.objects.filter(user_id=id):
        amount = WalletWithdrawalRequestTbl.objects.filter(user_id=id).aggregate(Sum('withdrawal_amt'))
        total_withdrawn_amount = {
            "withdrawal_done":1,
            "total_withdrawn_amount":amount,
        }
    else:
        total_withdrawn_amount = {
            "withdrawal_done":0,
        }

#the following code is for checking the pan verification
    if UserPanDetailTbl.objects.filter(user_id=id):
        user3 = UserPanDetailTbl.objects.filter(user_id=id)
        pan_verification = {
            "pan_available":1,
            "is_verified":user3.is_verified,
            'pan_no':user3.pancard_number,
        }
    else:
        pan_verification = {
            "pan_available":0,
        }

    if UserTransactionHistory.objects.filter(user_id=id):
        amount_deposit = UserTransactionHistory.objects.filter(user_id=id).aggregate(Sum('deposit_amt'))
        total_deposited_amount = {
            "deposition_done":1,
            "total_deposited_amount":amount_deposit,
        }
    else:
        total_deposited_amount = {
            "deposition_done":0,
        }

    # user1 = UserAccountDetailTbl.objects.get(user_id=id)
    # user2 = UserAccountDetailTbl.objects.get(user_id=id)
    # user2 = UserAccountDetailTbl.objects.get(user_id=id)
    # user2 = UserAccountDetailTbl.objects.get(user_id=id)
    #do try except here
    print(user1)
    print(id)
    # user = get_object_or_404(UsersTbl,user_id=id)
    # user1 = get_object_or_404(UserAccountDetailTbl,user_id=id)

    data = {
        "account_details":account_details,
        "personal_details":personal_details,
        'total_balance_amount':total_balance_amount,
        'total_withdrawn_amount':total_withdrawn_amount,
        'total_deposited_amount':total_deposited_amount,
        'pan_verification':pan_verification,
        }
    data1 = {"data": data}
    return JsonResponse(data1)



class Login(views.APIView):

    #why do I have to write the function name as post?
    def post(self,request,*args,**kwargs):
        if not request.data:
            return Response({'Error':"Please provide id/password"},status="400")

        id = request.data['id']
        password =request.data['password']

        try:
            user = AdminUsersTbl.objects.get(id = id, password=password)
            print(user)
        except user.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            #payload = jwt_payload_handler(user)

            payload = {
                'login':{
                'access':user.access,
                'email':user.login_email,
                'id':user.id,
                'phone':user.phone_no,
                }
            }

            jwt_token= {'token':jwt.encode(payload,settings.SECRET_KEY)}
            user_details={}
            user_details['token'] = jwt_token
            return Response(
            user_details,
            status=200,
            content_type="application/json"
            )
        else:
            return Response(
            json.dumps({'Error':"invalid credentials"}),
            status=400,
            content_type="application/json"
            )

class UserRetrieveAPIView(views.APIView):

    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = AdminSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenAuthentication(BaseAuthentication):

    model = None

    def get_model(self):
        return AdminUsersTbl

    def authenticate(self, request,id):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token=="null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token,id)

    def authenticate_credentials(self, token,id):
        model = self.get_model()
        payload = jwt.decode(token, settings.SECRET_KEY)
        id1 = payload['id']
        msg = {'Error': "Token mismatch",'status' :"401"}
        try:

            user1 = AdminUsersTbl.objects.get(
                id=id1,
            )

            #if not user.token['token'] == token:
            if not user1:
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except DoesNotExist:
            return HttpResponse({'Error': "Internal server error"}, status="500")


        user = get_object_or_404(UsersTbl,user_id=id)
        data = {"results":{
            "user_name":user.user_name,
            "user_id":user.user_id,
            "user_dob":user.user_dob,
            "first_name":user.first_name,
        }}
        data1 = {"data": data}
        return JsonResponse(data1)


    def authenticate_header(self, request):
        return 'Token'




#

class LoginView(views.APIView):

    @permission_classes((AllowAny,))
    def post(self,request,*args,**kwargs):
        id = request.data.get("id")
        password = request.data.get("password")
        if id is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status='400')
        #the following try except block is an great example for fetching an object from database using get.
        try:
            user = AdminUsersTbl.objects.get(id = id, password=password)
        except DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status='404')
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status='200')

# the following view is for posting comment :
@csrf_exempt
def comment(request,id):
        auth = get_authorization_header(request).split()
        try:
            token = auth[1]
            if token=="null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)


        model = AdminUsersTbl
        payload = jwt.decode(token, settings.SECRET_KEY)
        id1 = payload['login']['id']
        msg = {'Error': "Token mismatch",'status' :"401"}
        error_not_found = {'Error': "No User Found",'status' :"404"}


        print(id1)
        try:
            user1 = AdminUsersTbl.objects.get(
                id=id1,
            )

            #if not user.token['token'] == token:
            if not user1:
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except User.DoesNotExist:
            return HttpResponse({'Error': "Internal server error"}, status="500")

        print(id)
        if request.method=='GET':
            if(AdminCommentsTbl.objects.filter(user_id=id)):
                user5 = AdminCommentsTbl.objects.get(user_id=id)
                data = {'comment':user5.comment}
            else:
                data = {'comment':'no user found'}
            pprint(data)
            return(JsonResponse(data))
        elif request.method=='POST':
            comment = request.body
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            content = body['content']
            pprint(content)
            comments = comment[1]
            print(comments)
            if(AdminCommentsTbl.objects.filter(user_id=id)):
                AdminCommentsTbl.objects.filter(user_id=id).update(comment = comments)
                user5 = AdminCommentsTbl.objects.get(user_id=id)
                data = {'comment':user5.comment}
            else:
                data = {'comment':'no user found'}

            return JsonResponse(data)

#hey there write some production level code , also make this shit clean and readable.

# def users_detail(request,id):
#
#     #in the request block we get authorization token which we check to authenticate the request.
#     auth = get_authorization_header(request).split()
#
#     # learn more about getting headers and working on them.
#
#     try:
#         token = auth[1]
#         if token=="null":
#             msg = 'Null token not allowed'
#             raise exceptions.AuthenticationFailed(msg)
#     except UnicodeError:
#         msg = 'Invalid token header. Token string should not contain invalid characters.'
#         raise exceptions.AuthenticationFailed(msg)
#
#
#     model = AdminUsersTbl
#     payload = jwt.decode(token, settings.SECRET_KEY)
#
#     # print( "payload", payload)
#
#     id1 = payload['login']['id']
#     msg = {'Error': "Token mismatch",'status' :"401"}
#     error_not_found = {'Error': "No User Found",'status' :"404"}
#
#
#     print(id1)
#
# AUTHENTICATING:
#     try:
#         user1 = AdminUsersTbl.objects.get(
#             id=id1,
#         )
#
#         #if not user.token['token'] == token:
#         if not user1:
#             raise exceptions.AuthenticationFailed(msg)
#     except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
#         return HttpResponse({'Error': "Token is invalid"}, status="403")
#     except User.DoesNotExist:
#         return HttpResponse({'Error': "Internal server error"}, status="500")
#
# AUTHERIZING:
#     if UserTransactionHistory.objects.filter(user_id=id):#|UsersTbl.objects.filter(user_email=id)|UsersTbl.objects.filter(user_mobile=id):
#         user4 = UserTransactionHistory.objects.all(user_id=id)[:5]#|UsersTbl.objects.filter(user_email=id)|UsersTbl.objects.filter(user_mobile=id)
#         for(i in user):
#             transaction_details = {
#                 # "pan_available":1,
#                 "is_verified":user4.,
#                 'pan_no':user3.pancard_number,
#             }
#
