import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if len(dim) != 2 and len(position) != 2:
            return None
        if isinstance(array, np.ndarray) == False:
            return None
        dRow = dim[0]
        dCol = dim[1]
        pRow = position[0]
        pCol = position[1]
        newarray = array[pRow:pRow + dRow, pCol:pCol + dCol]
        return np.array(newarray)
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) == False:
            return None
        newarray = np.delete(np.array(array), n, axis=axis)
        return newarray

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) == False:
            return None
        i = 0
        newarray = array
        while i < n - 1:
            newarray = np.concatenate((newarray, array), axis=axis)
            i += 1
        return newarray

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(dim, tuple):
            array = ScrapBooker.juxtapose(self, array=array, n=dim[1], axis=1)
            array = ScrapBooker.juxtapose(self, array=array, n=dim[0], axis=0)
            
        return array