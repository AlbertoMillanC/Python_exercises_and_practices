from inspect import isfunction, ismethod
from typing import Any, Optional, Type, Union

from graphql.pyutils import Undefined

from ..utils.is_base_type import is_base_type
from ..utils.props import props
from .base import BaseArgument, BaseArgumentsObject
from .unmountedtype import UnmountedType


class Argument(BaseArgument):
    __slots__ = ()

    def __init__(
        self,
        _type: Optional[Type[Union[UnmountedType, Any]]] = None,
        default_value: Any = Undefined,
        required: bool = False,
        description: Optional[str] = None,
        **metadata: Any,
    ) -> None:
        super().__init__(
            _type=_type,
            default_value=default_value,
            required=required,
            description=description,
            **metadata,
        )


class ArgumentsMixin:
    @classmethod
    def __init_subclass_with_meta__(
        cls,
        arguments: Optional[Type[BaseArgumentsObject]] = None,
        **options: Any,
    ) -> None:
        if arguments:
            arguments_cls_name = f"{cls.__name__}Arguments"
            arguments = type(arguments_cls_name, (arguments,), {})
            cls._meta.arguments_class = arguments
        super().__init_subclass_with_meta__(**options)

        # Extract and attach the arguments
        cls._meta.fields.update(cls._meta.arguments_class.get_fields())

        # Set the resolver to look up the correct args
        original_resolver = cls._meta.resolver or props
        original_type_resolver = getattr(cls._meta, "type_resolver", None)

        async def wrapper_resolver(
            instance: Any, info: GraphQLResolveInfo, **kwargs: Any
        ) -> Any:
            if not kwargs:
                return await original_resolver(instance, info)
            args = cls._meta.arguments_class(kwargs)
            resolved = await original_resolver(instance, info, **args)
            if resolved is None and not original_type_resolver:
                return None
            return original_type_resolver(resolved) if original_type_resolver else resolved

        cls._meta.resolver = wrapper_resolver

        # Make sure that we # Define el esquema de GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)

# Define la vista de GraphiQL para explorar la API


class GraphQLView(graphene.View):
    def __init__(self, **kwargs):
        self.schema = schema
        self.batch = True
        super(GraphQLView, self).__init__(**kwargs)

    def dispatch_request(self, *args, **kwargs):
        return super(GraphQLView, self).dispatch_request(*args, **kwargs)


# Define la ruta para la vista de GraphiQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)
