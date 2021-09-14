#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from enum import IntEnum, Enum


class CustomEnum(Enum):
    @classmethod
    def valid(cls, value):
        try:
            cls(value)
            return True
        except:
            return False

    @classmethod
    def values(cls):
        return [member.value for member in cls.__members__.values()]

    @classmethod
    def names(cls):
        return [member.name for member in cls.__members__.values()]


class ComponentProviderName(CustomEnum):
    FATE_ALGORITHM = "fate_algorithm"
    AVATAR_ALGORITHM = "avatar_algorithm"
    FATE_FLOW_TOOLS = "fate_flow_tools"


class ModelStorage(CustomEnum):
    REDIS = "redis"
    MYSQL = "mysql"


class ModelOperation(CustomEnum):
    STORE = "store"
    RESTORE = "restore"
    EXPORT = "export"
    IMPORT = "import"
    LOAD = "load"
    BIND = "bind"


class ProcessRole(CustomEnum):
    DRIVER = "driver"
    WORKER = "worker"


class TagOperation(CustomEnum):
    CREATE = "create"
    RETRIEVE = "retrieve"
    UPDATE = "update"
    DESTROY = "destroy"
    LIST = "list"


class ResourceOperation(CustomEnum):
    APPLY = "apply"
    RETURN = "return"


class KillProcessRetCode(IntEnum, CustomEnum):
    KILLED = 0
    NOT_FOUND = 1
    ERROR_PID = 2


class InputSearchType(IntEnum, CustomEnum):
    UNKNOWN = 0
    TABLE_INFO = 1
    JOB_COMPONENT_OUTPUT = 2


class WorkerName(CustomEnum):
    TASK_EXECUTOR = "task_executor"
    TASK_INITIALIZER = "task_initializer"
    PROVIDER_REGISTRAR = "provider_registrar"
