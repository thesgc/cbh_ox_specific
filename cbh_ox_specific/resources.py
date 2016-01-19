from cbh_core_ws.resources import UserResource

class OxfordUserResource(UserResource):

    def build_filters():
        """here we swap an email search for a username search if the user is from Oxford"""
        pass


    def alter_list_data_to_serialize(self, bundle):
        """Here we add an extra user to the list of users found if no user has been found based on our webauth result"""
        pass
