import unittest
import hw5_cards



#########################################
##### Name:  Katie Henning          #####
##### Uniqname: khenning            #####
#########################################

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)
        

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        c3 = hw5_cards.Card(1, 12)
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        self.assertEqual(c3.rank_name, "Queen")
        return c3.rank_name, "Queen"
    
    def test_q2(self):
        c4 = hw5_cards.Card(1, 1)
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        self.assertEqual(c4.suit_name, "Clubs")
        return c4.suit_name, "Clubs"   
    

    def test_q3(self):
        c5 = hw5_cards.Card(3, 13)
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        
        self.assertEqual(c5.__str__(), "King of Spades")

        return c5.__str__(), "King of Spades"
    
    def test_q4(self):
        deck = hw5_cards.Deck()
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(len(deck.cards), 52)
        return len(deck.cards), 52

    def test_q5(self):
        deck = hw5_cards.Deck()
        dealt_card = deck.deal_card()
        card = hw5_cards.Card()
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertIsInstance(dealt_card, type(hw5_cards.Card()))
        return dealt_card, type(hw5_cards.Card())
    
    def test_q6(self):
        deck = hw5_cards.Deck()
        full_deck_size = len(deck.cards)
        dealt_card = deck.deal_card()
        
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(len(deck.cards), (full_deck_size-1))
        return len(deck.cards), (full_deck_size-1)  
    

    def test_q7(self):
        deck1 = hw5_cards.Deck()
        deck2 = hw5_cards.Deck()
        full_deck_size = len(deck2.cards)
        dealt_card = deck1.deal_card()
        one_less = deck1.cards
        deck1.replace_card(dealt_card)
        restored_deck = len(deck1.cards)

        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(restored_deck, full_deck_size)
        return restored_deck, full_deck_size
    
    def test_q8(self):

        
        deck1 = hw5_cards.Deck()
        deck2 = hw5_cards.Deck()
        deck3 = hw5_cards.Deck()
        full_deck_size = len(deck3.cards)
        dealt_card = deck1.deal_card()
        deck2.replace_card(dealt_card)
        ignore_card_deck = len(deck2.cards)

        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(ignore_card_deck, full_deck_size)
        return ignore_card_deck, full_deck_size



if __name__=="__main__":
    unittest.main()