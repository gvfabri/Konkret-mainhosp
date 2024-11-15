/* eslint-disable */
/* tslint:disable */
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

/** HTTPValidationError */
export interface HTTPValidationError {
  /** Detail */
  detail?: ValidationError[];
}

/** ValidationError */
export interface ValidationError {
  /** Location */
  loc: (string | number)[];
  /** Message */
  msg: string;
  /** Error Type */
  type: string;
}

import type { AxiosInstance, AxiosRequestConfig, AxiosResponse, HeadersDefaults, ResponseType } from "axios";
import axios from "axios";

export type QueryParamsType = Record<string | number, any>;

export interface FullRequestParams extends Omit<AxiosRequestConfig, "data" | "params" | "url" | "responseType"> {
  /** set parameter to `true` for call `securityWorker` for this request */
  secure?: boolean;
  /** request path */
  path: string;
  /** content type of request body */
  type?: ContentType;
  /** query params */
  query?: QueryParamsType;
  /** format of response (i.e. response.json() -> format: "json") */
  format?: ResponseType;
  /** request body */
  body?: unknown;
}

export type RequestParams = Omit<FullRequestParams, "body" | "method" | "query" | "path">;

export interface ApiConfig<SecurityDataType = unknown> extends Omit<AxiosRequestConfig, "data" | "cancelToken"> {
  securityWorker?: (
    securityData: SecurityDataType | null,
  ) => Promise<AxiosRequestConfig | void> | AxiosRequestConfig | void;
  secure?: boolean;
  format?: ResponseType;
}

export enum ContentType {
  Json = "application/json",
  FormData = "multipart/form-data",
  UrlEncoded = "application/x-www-form-urlencoded",
  Text = "text/plain",
}

export class HttpClient<SecurityDataType = unknown> {
  public instance: AxiosInstance;
  private securityData: SecurityDataType | null = null;
  private securityWorker?: ApiConfig<SecurityDataType>["securityWorker"];
  private secure?: boolean;
  private format?: ResponseType;

  constructor({ securityWorker, secure, format, ...axiosConfig }: ApiConfig<SecurityDataType> = {}) {
    this.instance = axios.create({ ...axiosConfig, baseURL: axiosConfig.baseURL || "" });
    this.secure = secure;
    this.format = format;
    this.securityWorker = securityWorker;
  }

  public setSecurityData = (data: SecurityDataType | null) => {
    this.securityData = data;
  };

  protected mergeRequestParams(params1: AxiosRequestConfig, params2?: AxiosRequestConfig): AxiosRequestConfig {
    const method = params1.method || (params2 && params2.method);

    return {
      ...this.instance.defaults,
      ...params1,
      ...(params2 || {}),
      headers: {
        ...((method && this.instance.defaults.headers[method.toLowerCase() as keyof HeadersDefaults]) || {}),
        ...(params1.headers || {}),
        ...((params2 && params2.headers) || {}),
      },
    };
  }

  protected stringifyFormItem(formItem: unknown) {
    if (typeof formItem === "object" && formItem !== null) {
      return JSON.stringify(formItem);
    } else {
      return `${formItem}`;
    }
  }

  protected createFormData(input: Record<string, unknown>): FormData {
    if (input instanceof FormData) {
      return input;
    }
    return Object.keys(input || {}).reduce((formData, key) => {
      const property = input[key];
      const propertyContent: any[] = property instanceof Array ? property : [property];

      for (const formItem of propertyContent) {
        const isFileType = formItem instanceof Blob || formItem instanceof File;
        formData.append(key, isFileType ? formItem : this.stringifyFormItem(formItem));
      }

      return formData;
    }, new FormData());
  }

  public request = async <T = any, _E = any>({
    secure,
    path,
    type,
    query,
    format,
    body,
    ...params
  }: FullRequestParams): Promise<AxiosResponse<T>> => {
    const secureParams =
      ((typeof secure === "boolean" ? secure : this.secure) &&
        this.securityWorker &&
        (await this.securityWorker(this.securityData))) ||
      {};
    const requestParams = this.mergeRequestParams(params, secureParams);
    const responseFormat = format || this.format || undefined;

    if (type === ContentType.FormData && body && body !== null && typeof body === "object") {
      body = this.createFormData(body as Record<string, unknown>);
    }

    if (type === ContentType.Text && body && body !== null && typeof body !== "string") {
      body = JSON.stringify(body);
    }

    return this.instance.request({
      ...requestParams,
      headers: {
        ...(requestParams.headers || {}),
        ...(type ? { "Content-Type": type } : {}),
      },
      params: query,
      responseType: responseFormat,
      data: body,
      url: path,
    });
  };
}

/**
 * @title FastAPI
 * @version 0.1.0
 */
export class Api<SecurityDataType extends unknown> extends HttpClient<SecurityDataType> {
  user = {
    /**
     * No description
     *
     * @tags user
     * @name AddUserUserPost
     * @summary Add User
     * @request POST:/user
     */
    addUserUserPost: (
      query: {
        /** Name */
        name: string;
        /** Cpf */
        cpf: string;
        /** Email */
        email: string;
        /** Password */
        password: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/user`,
        method: "POST",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name GetallUsersUserGet
     * @summary Getall Users
     * @request GET:/user
     */
    getallUsersUserGet: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/user`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name UpdateUserUserIdUpdatePut
     * @summary Update User
     * @request PUT:/user/{id}/update
     */
    updateUserUserIdUpdatePut: (
      id: string,
      query: {
        /** Cpf */
        cpf: string;
        /** Email */
        email: string;
        /** Password */
        password: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/user/${id}/update`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name GetUserUserIdGet
     * @summary Get User
     * @request GET:/user/{id}
     */
    getUserUserIdGet: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/user/${id}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name DeleteUserUserIdDelete
     * @summary Delete User
     * @request DELETE:/user/{id}
     */
    deleteUserUserIdDelete: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/user/${id}`,
        method: "DELETE",
        format: "json",
        ...params,
      }),
  };
  employee = {
    /**
     * No description
     *
     * @tags employee
     * @name AddEmployeeEmployeePost
     * @summary Add Employee
     * @request POST:/employee
     */
    addEmployeeEmployeePost: (
      query: {
        /** Name */
        name: string;
        /** Rg */
        rg: number;
        /** Cpf */
        cpf: number;
        /** Role */
        role: string;
        /** Salary */
        salary: number;
        /** Work Id */
        work_id: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/employee`,
        method: "POST",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags employee
     * @name GetallEmployeesEmployeeGet
     * @summary Getall Employees
     * @request GET:/employee
     */
    getallEmployeesEmployeeGet: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/employee`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags employee
     * @name UpdateEmployeeEmployeeIdUpdatePut
     * @summary Update Employee
     * @request PUT:/employee/{id}/update
     */
    updateEmployeeEmployeeIdUpdatePut: (
      id: string,
      query: {
        /** Salary */
        salary: number;
        /** Role */
        role: string;
        /** Work Id */
        work_id: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/employee/${id}/update`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags employee
     * @name GetEmployeeEmployeeIdGet
     * @summary Get Employee
     * @request GET:/employee/{id}
     */
    getEmployeeEmployeeIdGet: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/employee/${id}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags employee
     * @name DeleteEmployeeEmployeeIdDelete
     * @summary Delete Employee
     * @request DELETE:/employee/{id}
     */
    deleteEmployeeEmployeeIdDelete: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/employee/${id}`,
        method: "DELETE",
        format: "json",
        ...params,
      }),
  };
  work = {
    /**
     * No description
     *
     * @tags work
     * @name AddWorkWorkPost
     * @summary Add Work
     * @request POST:/work
     */
    addWorkWorkPost: (
      query: {
        /** Address */
        address: string;
        /** Photos */
        photos: any[];
        /** Proprietary */
        proprietary: string;
        /** Observations */
        observations: any[];
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/work`,
        method: "POST",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name GetallWorksWorkGet
     * @summary Getall Works
     * @request GET:/work
     */
    getallWorksWorkGet: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/work`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name AddPhotoWorkIdAddphotoPut
     * @summary Add Photo
     * @request PUT:/work/{id}/addphoto
     */
    addPhotoWorkIdAddphotoPut: (
      id: string,
      query: {
        /** Photo */
        photo: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/addphoto`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name RemovePhotoWorkIdRemovephotoPut
     * @summary Remove Photo
     * @request PUT:/work/{id}/removephoto
     */
    removePhotoWorkIdRemovephotoPut: (
      id: string,
      query: {
        /** Photo */
        photo: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/removephoto`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name AddObservationWorkIdAddobservationPut
     * @summary Add Observation
     * @request PUT:/work/{id}/addobservation
     */
    addObservationWorkIdAddobservationPut: (
      id: string,
      query: {
        /** Observation */
        observation: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/addobservation`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name RemoveObservationWorkIdRemoveobservationPut
     * @summary Remove Observation
     * @request PUT:/work/{id}/removeobservation
     */
    removeObservationWorkIdRemoveobservationPut: (
      id: string,
      query: {
        /** Observation */
        observation: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/removeobservation`,
        method: "PUT",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name GetWorkWorkIdGet
     * @summary Get Work
     * @request GET:/work/{id}
     */
    getWorkWorkIdGet: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name DeleteWorkWorkIdDelete
     * @summary Delete Work
     * @request DELETE:/work/{id}
     */
    deleteWorkWorkIdDelete: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}`,
        method: "DELETE",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name GetProprietaryWorkIdProprietaryGet
     * @summary Get Proprietary
     * @request GET:/work/{id}/proprietary
     */
    getProprietaryWorkIdProprietaryGet: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/proprietary`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags work
     * @name GetWorkersWorkIdWorkersGet
     * @summary Get Workers
     * @request GET:/work/{id}/workers
     */
    getWorkersWorkIdWorkersGet: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/work/${id}/workers`,
        method: "GET",
        format: "json",
        ...params,
      }),
  };
  proprietary = {
    /**
     * No description
     *
     * @tags Proprietary
     * @name AddProprietaryProprietaryPost
     * @summary Add Proprietary
     * @request POST:/proprietary
     */
    addProprietaryProprietaryPost: (
      query: {
        /** Name */
        name: string;
        /** Cpf */
        cpf: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/proprietary`,
        method: "POST",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Proprietary
     * @name GetallProprietariesProprietaryGet
     * @summary Getall Proprietaries
     * @request GET:/proprietary
     */
    getallProprietariesProprietaryGet: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/proprietary`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Proprietary
     * @name GetProprietaryProprietaryIdGet
     * @summary Get Proprietary
     * @request GET:/proprietary/{id}
     */
    getProprietaryProprietaryIdGet: (id: string, params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/proprietary/${id}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Proprietary
     * @name DeleteProprietaryProprietaryIdDelete
     * @summary Delete Proprietary
     * @request DELETE:/proprietary/{id}
     */
    deleteProprietaryProprietaryIdDelete: (id: string, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/proprietary/${id}`,
        method: "DELETE",
        format: "json",
        ...params,
      }),
  };
}
