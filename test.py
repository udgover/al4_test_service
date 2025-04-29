from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import (ProcessItem, Result,
                                                   ResultProcessTreeSection,
                                                   ResultSection, ResultJSONSection,
                                                   BODY_FORMAT, ResultImageSection)

from typing import Any, Dict, List, Optional, Set, Tuple
import time


class TestAL4(ServiceBase):
    def __init__(self, config: Optional[Dict] = None) -> None:
        super(TestAL4, self).__init__(config)

    def start(self) -> None:
        # ==================================================================
        # Startup actions:
        #   Your service might have to do some warming up on startup to make things faster
        # ==================================================================
        self.log.warning(f"start() from {self.service_attributes.name} service called")


    def execute(self, request: ServiceRequest) -> None:
        stime = time.time()
        while True:
            time.sleep(1)
            ctime = int(time.time() - stime)
            if ctime % 10 == 0:
                self.log.warning(f"Service is running for {ctime} seconds")
            if ctime > 180:
                break
        self.log.warning(f"Service has finished after running for {ctime} seconds")
        text_section = ResultSection('Output')
        try:
            text_section.add_line("Hello World")
        except Exception:
            self.log.exception("Error parsing output.")
        result.add_section(text_section)
