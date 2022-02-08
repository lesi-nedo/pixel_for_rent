import axios from "axios";
import getCookie from "./get_cookie";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const BASE_URL = "http://127.0.0.1:8000";
const csrftoken = getCookie("csrftoken");

const instance = axios.create({
  baseURL: BASE_URL,
  timeout: 1000 * 5,
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": csrftoken,
  },
});

function upload(
  formData: FormData,
  onUploadProgress: (event: ProgressEvent) => void,
  to_commit = "False"
): Promise<void> {
  const url = `${BASE_URL}/api-files/`;
  formData.append("to_commit", to_commit);
  return (
    instance
      .post(url, formData, { onUploadProgress })
      // get data
      /* eslint-disable  @typescript-eslint/no-explicit-any */

      .then((x: any) => x.data)
  );
}

export { upload };
