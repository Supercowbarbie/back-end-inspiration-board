from app import db
from sqlalchemy.orm import relationship
from flask import current_app

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    card = db.relationship("Card", back_populates="board", lazy=True)


    def board_json(self):
        return {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }

    def return_board_cards(self):
        cards_list = []
        for card in self.card:
            cards_list.append(card.card_json())
        return{
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner,
            "cards": cards_list
        }