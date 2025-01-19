import logging
import traceback
from datetime import datetime

import inspect

class HTMLDetailsFormatter(logging.Formatter):
    def format(self, record):
        
        record.asctime = self.formatTime(record, self.datefmt)

        # it's a short string of log message
        summary = f"{record.asctime} - {record.levelname} - {record.getMessage()}"
        
        # local context details
        context = self.get_call_context()

        # Call stack
        stack = traceback.format_stack()
        stack_str = "".join(stack)

        # HTML formatted output
        html_output = f"""
<details>
    <summary>{summary}</summary>
    <details>
      <summary>Контекст</summary>
      <pre>
{context}</pre>
    </details>
    <pre>
{stack_str}
    </pre>
</details>
        """
        return html_output.strip()

    def get_call_context(self):
        """
        Return the context of the last called function (local variables and arguments).
        """

        frame = inspect.currentframe()

        # Get the frame of the caller
        while frame:
            if frame.f_code.co_name == "log" or frame.f_code.co_name == "_log":
                frame = frame.f_back
            else:
                break

        if frame:
            # Get local variables
            args, _, _, locals_dict = inspect.getargvalues(frame)
            context = "Local cotnext:\n"
            for arg in args:
                context += f"{arg}: {locals_dict[arg]}\n"
            for var, value in locals_dict.items():
                if var not in args:
                    context += f"{var}: {value}\n"
            return context
        return "No local cotnext"
    
    @staticmethod
    def initLogger(output='logs/errors.html', log_level=logging.ERROR, logger_name='html_details_logger'):
        # logger setup
        logger = logging.getLogger( logger_name )
        # logger.setLevel(logging.DEBUG)

        error_handler = logging.FileHandler(output, mode='w', encoding='utf-8')
        error_handler.setLevel( log_level )
        error_formatter = HTMLDetailsFormatter(fmt='%(asctime)s', datefmt='%Y-%m-%d %H:%M:%S')
        error_handler.setFormatter(error_formatter)
        logger.addHandler(error_handler)