class ActUtlType:
    @property
    def ActLogicalStationNumber(self) -> int: ...
    @ActLogicalStationNumber.setter
    def ActLogicalStationNumber(self, value: int): ...
    @property
    def ActPassword(self) -> str: ...
    @ActPassword.setter
    def ActPassword(self, value: str): ...
    def Open(self): ...
    def Close(self): ...
    def ReadDeviceBlock2(self, device: str, size: int, data: bytearray = None, offset: int = 0): ...
    def WriteDeviceBlock2(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadDeviceRandom2(self, device: str, size: int, data: bytearray = None, offset: int = 0): ...
    def WriteDeviceRandom2(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def CheckControl(self): ...
    def GetCpuType(self) -> tuple[str, int]: ...
    def SetCpuStatus(self, operation: int): ...
    def ReadDeviceBlock(self, device: str, size: int, data: bytearray = None, offset: int = 0): ...
    def WriteDeviceBlock(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadDeviceRandom(self, device: str, size: int, data: bytearray = None, offset: int = 0): ...
    def WriteDeviceRandom(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadBuffer(self, startio: int, address: int, size: int, data: bytearray = None, offset: int = 0): ...
    def WriteBuffer(self, startio: int, address: int, size: int, data: bytearray, offset: int = 0): ...
    def GetClockData(self) -> tuple[int, int, int, int, int, int, int]: ...
    def SetClockData(self, year: int, month: int, day: int, day_of_week: int, hour: int, minute: int, second: int): ...
    def SetDevice(self, value: int): ...
    def GetDevice(self) -> int: ...
    def GetDevice2(self) -> int: ...
    def SetDevice2(self, value: int): ...


class ActProgType:
    @property
    def ActNetworkNumber(self) -> int: ...
    @ActNetworkNumber.setter
    def ActNetworkNumber(self, value: int): ...
    @property
    def ActStationNumber(self) -> int: ...
    @ActStationNumber.setter
    def ActStationNumber(self, value: int): ...
    @property
    def ActUnitNumber(self) -> int: ...
    @ActUnitNumber.setter
    def ActUnitNumber(self, value: int): ...
    @property
    def ActConnectUnitNumber(self) -> int: ...
    @ActConnectUnitNumber.setter
    def ActConnectUnitNumber(self, value: int): ...
    @property
    def ActIONumber(self) -> int: ...
    @ActIONumber.setter
    def ActIONumber(self, value: int): ...
    @property
    def ActCpuType(self) -> int: ...
    @ActCpuType.setter
    def ActCpuType(self, value: int): ...
    @property
    def ActPortNumber(self) -> int: ...
    @ActPortNumber.setter
    def ActPortNumber(self, value: int): ...
    @property
    def ActBaudRate(self) -> int: ...
    @ActBaudRate.setter
    def ActBaudRate(self, value: int): ...
    @property
    def ActDataBits(self) -> int: ...
    @ActDataBits.setter
    def ActDataBits(self, value: int): ...
    @property
    def ActParity(self) -> int: ...
    @ActParity.setter
    def ActParity(self, value: int): ...
    @property
    def ActStopBits(self) -> int: ...
    @ActStopBits.setter
    def ActStopBits(self, value: int): ...
    @property
    def ActControl(self) -> int: ...
    @ActControl.setter
    def ActControl(self, value: int): ...
    @property
    def ActHostAddress(self) -> str: ...
    @ActHostAddress.setter
    def ActHostAddress(self, value: str): ...
    @property
    def ActCpuTimeOut(self) -> int: ...
    @ActCpuTimeOut.setter
    def ActCpuTimeOut(self, value: int): ...
    @property
    def ActTimeOut(self) -> int: ...
    @ActTimeOut.setter
    def ActTimeOut(self, value: int): ...
    @property
    def ActSumCheck(self) -> int: ...
    @ActSumCheck.setter
    def ActSumCheck(self, value: int): ...
    @property
    def ActSourceNetworkNumber(self) -> int: ...
    @ActSourceNetworkNumber.setter
    def ActSourceNetworkNumber(self, value: int): ...
    @property
    def ActSourceStationNumber(self) -> int: ...
    @ActSourceStationNumber.setter
    def ActSourceStationNumber(self, value: int): ...
    @property
    def ActDestinationPortNumber(self) -> int: ...
    @ActDestinationPortNumber.setter
    def ActDestinationPortNumber(self, value: int): ...
    @property
    def ActDestinationIONumber(self) -> int: ...
    @ActDestinationIONumber.setter
    def ActDestinationIONumber(self, value: int): ...
    @property
    def ActMultiDropChannelNumber(self) -> int: ...
    @ActMultiDropChannelNumber.setter
    def ActMultiDropChannelNumber(self, value: int): ...
    @property
    def ActThroughNetworkType(self) -> int: ...
    @ActThroughNetworkType.setter
    def ActThroughNetworkType(self, value: int): ...
    @property
    def ActIntelligentPreferenceBit(self) -> int: ...
    @ActIntelligentPreferenceBit.setter
    def ActIntelligentPreferenceBit(self, value: int): ...
    @property
    def ActDidPropertyBit(self) -> int: ...
    @ActDidPropertyBit.setter
    def ActDidPropertyBit(self, value: int): ...
    @property
    def ActDsidPropertyBit(self) -> int: ...
    @ActDsidPropertyBit.setter
    def ActDsidPropertyBit(self, value: int): ...
    @property
    def ActPacketType(self) -> int: ...
    @ActPacketType.setter
    def ActPacketType(self, value: int): ...
    @property
    def ActPassword(self) -> str: ...
    @ActPassword.setter
    def ActPassword(self, value: str): ...
    @property
    def ActTargetSimulator(self) -> int: ...
    @ActTargetSimulator.setter
    def ActTargetSimulator(self, value: int): ...
    @property
    def ActUnitType(self) -> int: ...
    @ActUnitType.setter
    def ActUnitType(self, value: int): ...
    @property
    def ActProtocolType(self) -> int: ...
    @ActProtocolType.setter
    def ActProtocolType(self, value: int): ...
    def Open(self): ...
    def Close(self): ...
    def ReadDeviceBlock2(self, device: str, size: int, data: bytearray = None, offset: int = 0) -> bytearray: ...
    def WriteDeviceBlock2(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadDeviceRandom2(self, device: str, size: int, data: bytearray = None, offset: int = 0) -> bytearray: ...
    def WriteDeviceRandom2(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def CheckControl(self): ...
    def GetCpuType(self) -> tuple[str, int]: ...
    def SetCpuStatus(self, operation: int): ...
    def ReadDeviceBlock(self, device: str, size: int, data: bytearray = None, offset: int = 0) -> bytearray: ...
    def WriteDeviceBlock(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadDeviceRandom(self, device: str, size: int, data: bytearray = None, offset: int = 0) -> bytearray: ...
    def WriteDeviceRandom(self, device: str, size: int, data: bytearray, offset: int = 0): ...
    def ReadBuffer(self, startio: int, address: int, size: int, data: bytearray = None, offset: int = 0) -> bytearray: ...
    def WriteBuffer(self, startio: int, address: int, size: int, data: bytearray, offset: int = 0): ...
    def GetClockData(self) -> tuple[int, int, int, int, int, int, int]: ...
    def SetClockData(self, year: int, month: int, day: int, day_of_week: int, hour: int, minute: int, second: int): ...
    def SetDevice(self, value: int): ...
    def GetDevice(self) -> int: ...
    def GetDevice2(self) -> int: ...
    def SetDevice2(self, value: int): ...