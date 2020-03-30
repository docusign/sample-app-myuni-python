import React from "react";
import { useTranslation } from "react-i18next";
import parse from "html-react-parser";

export const About = () => {
  const { t } = useTranslation("About");
  return (
    <div className="container">
      <br></br>

      <h2 id="sample-app">{t("Title")}</h2>
      <blockquote>{parse(t("Description"))}</blockquote>

      <div className="row">
        <div className="col-md-6">
          <p>
            <strong>
              {t("SourceButton")}
              <a
                target="_blank"
                href="https://github.com/docusign/Sigma-EducationApp/"
                rel="noopener noreferrer"
              >
                {t("GitHubLink")}
              </a>
            </strong>
          </p>
          <br></br>
          <br></br>

          {parse(t("Features"))}
        </div>
        <div className="col-md-6">
          <br></br>
          <br></br>
          <h4> {t("ToolsandLinks")}</h4>

          <h5> {t("DeveloperCenter")}</h5>
          <a
            target="_blank"
            href="https://developers.docusign.com"
            rel="noopener noreferrer"
          >
            {t("DeveloperCenterLink")}
          </a>

          <h5>{t("APICodeExamples")}</h5>
          <a
            target="_blank"
            href="https://developers.docusign.com/esign-rest-api/code-examples"
            rel="noopener noreferrer"
          >
            {t("APICodeExamplesLink")}
          </a>

          <h5>{t("ESignatureDocumentation")}</h5>
          <a
            target="_blank"
            href="https://developers.docusign.com/esign-rest-api/reference"
            rel="noopener noreferrer"
          >
            {t("ESignatureDocumentationLink")}
          </a>

          <h5> {t("DeveloperCommunity")}</h5>
          <a
            target="_blank"
            href="http://stackoverflow.com/questions/tagged/docusignapi"
            rel="noopener noreferrer"
          >
            {t("DeveloperCommunityLink")}
          </a>
        </div>
      </div>
      {parse(t("AboutDocuSign"))}

      <br></br>

      <p>
        <a href="http://www.docusign.com/"> {t("DocuSignLink")}</a>
      </p>
    </div>
  );
};
