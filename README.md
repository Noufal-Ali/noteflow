**🧠 NOTEFLOW - AI-Powered Notes Backend**
--------------------------------------------

**🚀 Overview**
-----------------
NoteFlow is a scalable backend system built using Django REST Framework that allows users to manage notes with 
advanced features like AI-powered summarization and contextual chat.

This project integrates basic CRUD operations with AI capabilities and production-level backend design patterns.

-----------------------------------------------------------------------------------------------------------------------

**🧱Tech Stack**
-----------------
**Backend:** Python, Django, Django REST Framework.

**Database:** PostgreSQL

**Authentication:** JWT(SimpleJWT)

**AI Integration:** OpenAI, Gemini, Mock(Provider-based architecture)

-------------------------------------------------------------------------------------------------------------------------

**🔥 Features**
-----------------

**🔐 Authentication & User Management**
-----------------------------------------
- JWT-based authentication
- Custom user model
- Role-based access control(Admin, Manger, Employee)
--------------------------------------------------------------------------------------------------------------------------

**📋 Note Management**
------------------------
- Create, update, and delete notes
- Flexible tag system with automatic tag creation and association
- Pagination, filtering, searching, and ordering
---------------------------------------------------------------------------------------------------------------------------

**🤖 AI Features**
-------------------
- **Summarize Notes** using AI
- **Chat with Notes** (context-aware response)
- Provider-based AI system (switch between OpenAI, Gemini, or Mock via environment variable)
---------------------------------------------------------------------------------------------------------------------------

**⚠️Error Handling**
---------------------
- Structured error responses with custom error responses.
- Field-level validation errors
- Global exception handler
---------------------------------------------------------------------------------------------------------------------------

**🧠 Architecture Highlights**
-------------------------------
- Clean separation of concerns (views, serializers, services)
- Provider-based AI layer
- Scalable and production-ready API design
----------------------------------------------------------------------------------------------------------------------------

**🔗API Endpoints (Sample)**
-----------------------------
- /accounts/register/
- /ai/summarize/
- /ai/chat/
-----------------------------------------------------------------------------------------------------------------------------

**⚙️ Setup Information**
-------------------------

```bash
cd NoteFlow

python -m venv venv
venv\Scripts\activate #Windows

pip install -r requirements.txt
```
