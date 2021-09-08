from datetime import datetime, timedelta
import requests
import pprint

class HistoryManager:
    reqManager =  None
    def __init__(self, reqManager):
        self.reqManager = reqManager
        pass

    def getPageList(self, filter=None):
        endpoint = "/api/pages"
        if filter!=None:
            endpoint += "?%s" % filter
        return self.reqManager.get(endpoint)

    def getPageDetail(self, pageId):
        endpoint = "/api/pages/%d" % pageId
        return self.reqManager.get(endpoint)

    def getBookList(self, filter=None):
        endpoint = "/api/books"
        if filter!=None:
            endpoint += "?%s" % filter
        return self.reqManager.get(endpoint)

    def getBookDetail(self, bookId):
        endpoint = "/api/books/%d" % bookId
        return self.reqManager.get(endpoint)

    def getHistoryUrl(self, bookId, pageSlug):
        bookSlug = self.getBookDetail(bookId)["slug"]
        endpoint = "/books/%s/page/%s" % (bookSlug, pageSlug)
        return endpoint

    def createPage(self, bookId, chapterId, name, html):
        data = {
            "book_id":bookId, 
            "name":name, 
            "html":html
        }

        if chapterId>0:
            data["chapter_id"] = chapterId

        endpoint = "/api/pages"
        return self.reqManager.post(endpoint, data)

    def updatePage(self, pageId, html):
        data = {
            "html":html
        }
        endpoint = "/api/pages/%d" % pageId
        return self.reqManager.put(endpoint, data)

    def updateCompleteHistory(self):
        targetDateFilter = "filter[created_at:gt]=" + datetime.strftime(datetime.now() - timedelta(days=30), "%Y-%m-%d")
        pages = self.getPageList(targetDateFilter)["data"]

        for page in pages:
            historyDetail = self.getPageDetail(page["id"])
            if len(historyDetail["tags"])<1 or historyDetail["tags"][0]["name"] != "status":
                continue

            status = historyDetail["tags"][0]["value"]
            updatedAt = historyDetail["updated_at"].split(" ")[0]
            wikiHistoryId = self.getBookList("filter[name:eq]=Wiki History")["data"][0]["id"]
            pageTitle = updatedAt + "-History"
            # 완료가 된 글 처리
            if status=="completed":
                historyList = self.getPageList("filter[name:eq]=%s" % pageTitle)["data"]
                if len(historyList) == 0:
                    # create history page
                    print("History 페이지 생성 : " + pageTitle)
                    print(self.createPage(bookId=wikiHistoryId, chapterId=0, name=pageTitle, html="<h3>history page</h3><br>"))


                historyPageId = self.getPageList("filter[name:eq]=%s" % pageTitle)["data"][0]["id"]
                historyPageHtml = self.getPageDetail(historyPageId)["html"]
                if historyPageHtml.find(historyDetail["name"])<0:
                    historyPageHtml += "<br>"
                    historyPageHtml += "%s > <a href=\"%s\">상세보기</a>" % (historyDetail["name"], self.getHistoryUrl(historyDetail["book_id"], historyDetail["slug"]))

                    # history update
                    data = self.updatePage(historyPageId, historyPageHtml)
                    print(data)
                    print(pageTitle + " 페이지 업데이트...!")


                
                
                