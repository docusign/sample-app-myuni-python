import React from "react";
import { useTranslation } from "react-i18next";
import parse from "html-react-parser";

export const ApiDescription = () => {
  const { t } = useTranslation("History");
  const style = {
    display: "flex",
    alignItems: "flex-start"
  };

  return (
    <div className="col-lg-6 pt-2 pb-4" style={style}>
      <div id="accordion">
        <div className="card">
          <div className="card-header" id="headingOne">
            <h5 className="mb-0">
              <button
                className="btn btn-link"
                data-toggle="collapse"
                data-target="#collapseOne"
                aria-expanded="false"
                aria-controls="collapseOne"
              >
                {t("ApiDecription.SeeMore")}
              </button>
            </h5>
          </div>
          <div
            id="collapseOne"
            className="collapse"
            aria-labelledby="headingOne"
            data-parent="#accordion"
          >
            <div className="card-body">
              {parse(t("ApiDecription.CodeFlow"))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
