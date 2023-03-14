from  api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key (email, password)
    assert status == 200
    assert "key" in result

def test_get_all_pets_with_valid_key(filter=""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result) > 0



def test_post_add_new_pets_with_valid_data(name='Альфа', animal_type='Лайка', age='3',pet_photo='images/dog.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['id'] is not None
    assert isinstance(result['id'], str)

def test_update_info_about_pet(name = "Альфа2.0", animal_type = "двортерьер", age = "5"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, myPets = pf.get_list_of_pets(auth_key, filter="my_pets")

    pet_id = next(pet['id'] for pet in myPets if pet['name'] == 'Альфа')
    assert pet_id is not None
    status, result = pf.update_info_about_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result["name"] == name



def test_delete_pet_with_valid_pet_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, myPets = pf.get_list_of_pets(auth_key, filter="my_pets")

    pet_id = next(pet['id'] for pet in myPets if pet['name'] == 'Альфа')
    assert pet_id is not None
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200