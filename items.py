def item(tag, name, description):
  return {'tag': tag, 'name': name, 'description': description}

def mage_chest_key_item() -> dict:
  return item('mage_chest_key','Chave do Baú do Mago', 'Abra o Baú do Mago para encontrar o tesouro!')
