import bestv8
from abc import ABCMeta, abstractmethod
import six


@six.add_metaclass(ABCMeta)
class AbstractRuntimeContext(object):
    '''
    Abstract base class for runtime context class.
    '''
    def exec_(self, source, recv_size=20000):
        '''Execute source by JavaScript runtime and return all output to stdout as a string.

        source -- JavaScript code to execute.
        '''
        if not self.is_available():
            raise bestv8.RuntimeUnavailableError
        return self._exec_(source, recv_size=recv_size)

    def eval(self, source, recv_size=20000):
        '''Evaluate source in JavaScript runtime.

        source -- JavaScript code to evaluate.
        '''
        if not self.is_available():
            raise bestv8.RuntimeUnavailableError
        return self._eval(source, recv_size=recv_size)

    def call(self, name, *args, recv_size=20000):
        '''Call a JavaScript function in context.

        name -- Name of funtion object to call
        args -- Arguments for the funtion object
        '''
        if not self.is_available():
            raise bestv8.RuntimeUnavailableError
        return self._call(name, *args, recv_size=recv_size)

    @abstractmethod
    def is_available(self):
        raise NotImplementedError

    @abstractmethod
    def _exec_(self, source, recv_size=20000):
        raise NotImplementedError

    @abstractmethod
    def _eval(self, source, recv_size=20000):
        raise NotImplementedError

    @abstractmethod
    def _call(self, name, *args, recv_size=20000):
        raise NotImplementedError