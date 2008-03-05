from vanillaBase import VanillaBaseControl


class SearchBox(VanillaBaseControl):
    
    """
    A text entry field similar to the search field in Safari.
    
    pre.
    from vanilla import *
     
    class SearchBoxDemo(object):
            
        def __init__(self):
            self.w = Window((100, 42))
            self.w.searchBox = SearchBox((10, 10, -10, 22),
                                    callback=self.searchBoxCallback)
            self.w.open()
            
        def searchBoxCallback(self, sender):
            print 'search box entry!', sender.get()
        
    SearchBoxDemo()
    """
    
    def __init__(self, posSize, text="", callback=None, sizeStyle="regular"):
        """
        *posSize* Tuple of form (left, top, width, height) representing the position and size of the search box.

        |\\3. *Standard Dimensions* |
        | Regular | H | 22          |
        | Small   | H | 19          |
        | Mini    | H | 15          |
        
        *text* The text to be displayed in the search box.
        
        *callback* The method to be called when the user presses the search box.
        
        *sizeStyle* A string representing the desired size style of the search box. The options are:
        
        | "regular" |
        | "small"   |
        | "mini"    |
        """
        self._setupView("NSSearchField", posSize, callback=callback)
        self._setSizeStyle(sizeStyle)
        self._nsObject.setStringValue_(text)
    
    def getNSSearchField(self):
        """
        Return the _NSSearchField_ that this object wraps.
        """
        return self._nsObject
    
    def get(self):
        """
        Get the contents of the search box.
        """
        return self._nsObject.stringValue()

    def set(self, value):
        """
        Set the contents of the search box.
        
        *value* A string representing the contents of the search box.
        """
        self._nsObject.setStringValue_(value)