#include "Core/mvPythonModule.h"
#include "Core/mvApp.h"
#include "Core/mvPythonTranslator.h"

namespace Marvel {

	PyObject* ShowLogger(PyObject* self, PyObject* args)
	{

		mvApp::GetApp()->showLogger();

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* SetLogLevel(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		int level;

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::Integer, "level")
			});

		if(!pl.parse(__FUNCTION__, &level))
			return Py_None;

		mvApp::GetApp()->setLogLevel(level);

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* Log(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		const char* message;
		const char* level = "TRACE";

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::String, "message"),
			mvPythonDataElement(mvPythonDataType::Optional, ""),
			mvPythonDataElement(mvPythonDataType::String, "level")
			});

		if(!pl.parse(__FUNCTION__, &message, &level))
			return Py_None;

		mvApp::GetApp()->Log(std::string(message), std::string(level));

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* LogDebug(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		const char* message;

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::String, "level")
			});

		if (!pl.parse(__FUNCTION__, &message))
			return Py_None;

		mvApp::GetApp()->LogDebug(std::string(message));

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* LogInfo(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		const char* message;

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::String, "level")
			});

		if (!pl.parse(__FUNCTION__, &message))
			return Py_None;

		mvApp::GetApp()->LogInfo(std::string(message));

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* LogWarning(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		const char* message;

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::String, "level")
			});

		if (!pl.parse(__FUNCTION__, &message))
			return Py_None;

		mvApp::GetApp()->LogWarning(std::string(message));

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* LogError(PyObject* self, PyObject* args, PyObject* kwargs)
	{
		const char* message;

		auto pl = mvPythonTranslator(args, kwargs, {
			mvPythonDataElement(mvPythonDataType::String, "level")
			});

		if (!pl.parse(__FUNCTION__, &message))
			return Py_None;

		mvApp::GetApp()->LogError(std::string(message));

		Py_INCREF(Py_None);

		return Py_None;
	}

	PyObject* ClearLog(PyObject* self, PyObject* args, PyObject* kwargs)
	{

		mvApp::GetApp()->ClearLog();

		Py_INCREF(Py_None);

		return Py_None;
	}

	void CreateLoggerInterface(mvPythonModule& pyModule, PyObject* (*initfunc)())
	{
		pyModule.addMethod(ShowLogger, "Not Documented");
		pyModule.addMethod(SetLogLevel, "Not Documented");
		pyModule.addMethod(Log, "Not Documented");
		pyModule.addMethod(LogDebug, "Not Documented");
		pyModule.addMethod(LogInfo, "Not Documented");
		pyModule.addMethod(LogWarning, "Not Documented");
		pyModule.addMethod(LogError, "Not Documented");
		pyModule.addMethod(ClearLog, "Not Documented");

		PyImport_AppendInittab(pyModule.getName(), initfunc);
	}
}