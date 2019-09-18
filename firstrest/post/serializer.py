from .models import Post
from rest_framework import serializers
#json파일을 직렬화하는 프레임워크 



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'
                # '__all__'  # 고유로 부여된 'id'값까지 추가
                #['id','title', 'body']

        # 수정이 불가능하고 읽기만 가능하게 하는 항목 
        # 튜플로 적용해서 순서변경이 안되게 하기
        read_only_fields = ('title',) 