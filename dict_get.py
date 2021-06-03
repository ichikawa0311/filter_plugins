from ansible.errors import AnsibleError

class FilterModule(object):

    def dict_get(self, a_dict, a_key):
        if( not isinstance(a_dict,dict) ):
            raise AnsibleError('the parameter is not dict')
        if( not (a_key in a_dict.keys() ) ):
            raise AnsibleError("dict doesnt have a key "+a_key)
        return a_dict[a_key]
    def filters(self):
        return {
            # 左側がPlaybook内で使用するフィルター名、右側が紐付ける関数名。
            'dict_get': self.dict_get,
        }
