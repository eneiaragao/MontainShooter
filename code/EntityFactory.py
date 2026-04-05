#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.const import WIN_WIDTH


class EntityFactory: # Removida a herança de Level

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg': # Corrigida a sintaxe do case
                list_bg = []
                for i in range(7):
                    # Corrigido o nome da string e a passagem da posição
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg