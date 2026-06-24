# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTodoTodosPost**](DefaultApi.md#createtodotodospost) | **POST** /todos | Create Todo |
| [**deleteTodoTodosTodoIdDelete**](DefaultApi.md#deletetodotodostodoiddelete) | **DELETE** /todos/{todo_id} | Delete Todo |
| [**getTodoTodosTodoIdGet**](DefaultApi.md#gettodotodostodoidget) | **GET** /todos/{todo_id} | Get Todo |
| [**getTodosTodosGet**](DefaultApi.md#gettodostodosget) | **GET** /todos | Get Todos |
| [**loginLoginPost**](DefaultApi.md#loginloginpost) | **POST** /login | Login |
| [**readCurrentUserMeGet**](DefaultApi.md#readcurrentusermeget) | **GET** /me | Read Current User |
| [**readRootGet**](DefaultApi.md#readrootget) | **GET** / | Read Root |
| [**registerRegisterPost**](DefaultApi.md#registerregisterpost) | **POST** /register | Register |
| [**updateTodoTodosTodoIdPut**](DefaultApi.md#updatetodotodostodoidput) | **PUT** /todos/{todo_id} | Update Todo |



## createTodoTodosPost

> any createTodoTodosPost(todo)

Create Todo

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { CreateTodoTodosPostRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // Todo
    todo: ...,
  } satisfies CreateTodoTodosPostRequest;

  try {
    const data = await api.createTodoTodosPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **todo** | [Todo](Todo.md) |  | |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteTodoTodosTodoIdDelete

> any deleteTodoTodosTodoIdDelete(todoId)

Delete Todo

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { DeleteTodoTodosTodoIdDeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // number
    todoId: 56,
  } satisfies DeleteTodoTodosTodoIdDeleteRequest;

  try {
    const data = await api.deleteTodoTodosTodoIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **todoId** | `number` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTodoTodosTodoIdGet

> any getTodoTodosTodoIdGet(todoId)

Get Todo

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { GetTodoTodosTodoIdGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // number
    todoId: 56,
  } satisfies GetTodoTodosTodoIdGetRequest;

  try {
    const data = await api.getTodoTodosTodoIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **todoId** | `number` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTodosTodosGet

> any getTodosTodosGet()

Get Todos

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { GetTodosTodosGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.getTodosTodosGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## loginLoginPost

> any loginLoginPost(username, password, grantType, scope, clientId, clientSecret)

Login

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { LoginLoginPostRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    username: username_example,
    // string
    password: password_example,
    // string (optional)
    grantType: grantType_example,
    // string (optional)
    scope: scope_example,
    // string (optional)
    clientId: clientId_example,
    // string (optional)
    clientSecret: clientSecret_example,
  } satisfies LoginLoginPostRequest;

  try {
    const data = await api.loginLoginPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | `string` |  | [Defaults to `undefined`] |
| **password** | `string` |  | [Defaults to `undefined`] |
| **grantType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **scope** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **clientId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **clientSecret** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readCurrentUserMeGet

> any readCurrentUserMeGet()

Read Current User

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { ReadCurrentUserMeGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure OAuth2 access token for authorization: OAuth2PasswordBearer password
    accessToken: "YOUR ACCESS TOKEN",
  });
  const api = new DefaultApi(config);

  try {
    const data = await api.readCurrentUserMeGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**any**

### Authorization

[OAuth2PasswordBearer password](../README.md#OAuth2PasswordBearer-password)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readRootGet

> any readRootGet()

Read Root

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { ReadRootGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.readRootGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## registerRegisterPost

> any registerRegisterPost(userCreate)

Register

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { RegisterRegisterPostRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // UserCreate
    userCreate: ...,
  } satisfies RegisterRegisterPostRequest;

  try {
    const data = await api.registerRegisterPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userCreate** | [UserCreate](UserCreate.md) |  | |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateTodoTodosTodoIdPut

> any updateTodoTodosTodoIdPut(todoId, todo)

Update Todo

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '';
import type { UpdateTodoTodosTodoIdPutRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DefaultApi();

  const body = {
    // number
    todoId: 56,
    // Todo
    todo: ...,
  } satisfies UpdateTodoTodosTodoIdPutRequest;

  try {
    const data = await api.updateTodoTodosTodoIdPut(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **todoId** | `number` |  | [Defaults to `undefined`] |
| **todo** | [Todo](Todo.md) |  | |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

