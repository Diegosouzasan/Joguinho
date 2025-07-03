#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

from pygame.examples.video import backgrounds

from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory(ABC):

    @abstractmethod
    def get_entity(self: str, position=(0, 0)):
        match self:
            case 'Level1bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
        return None


