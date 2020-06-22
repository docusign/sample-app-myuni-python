import axios from "./interceptors";
import { handleResponse, handleError } from "./apiHelper";

export async function requestMinorChange(request) {
  try {
    const response = await axios.post(
      process.env.REACT_APP_API_BASE_URL + "/requests/minormajor",
      request,
      {
        withCredentials: true
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}

export async function signUpForExtracurricularActivity(request) {
  try {
    const response = await axios.post(
      process.env.REACT_APP_API_BASE_URL + "/requests/activity",
      request,
      {
        withCredentials: true
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}

export async function requestTranscript(request) {
  try {
    const response = await axios.post(
      process.env.REACT_APP_API_BASE_URL + "/requests/transcript",
      request,
      {
        withCredentials: true
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}

export async function getStatus(fromDate) {
  try {
    const response = await axios.get(
      process.env.REACT_APP_API_BASE_URL + "/requests",
      {
        params: {
          "from-date": fromDate
        },
        withCredentials: true
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}

export async function getStatusDocument(envelopId, documentId) {
  try {
    const response = await axios.get(
      process.env.REACT_APP_API_BASE_URL + "/requests/download",
      {
        params: {
          "envelope-id": envelopId,
          "document-id": documentId
        },
        withCredentials: true,
        responseType: "blob"
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}

export async function getCliwrapForRequestTranscript(request) {
  try {
    const response = await axios.post(
      process.env.REACT_APP_API_BASE_URL + "/clickwraps/transcript",
      request,
      {
        withCredentials: true
      }
    );
    return handleResponse(response);
  } catch (error) {
    handleError(error);
  }
}