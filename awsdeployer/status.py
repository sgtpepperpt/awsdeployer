import enum


class Common(enum.Enum):
    Created = (201, 'Created')
    Accepted = (202, 'Accepted')
    NoContent = (204, 'NoContent')
    BadRequest = (400, 'BadRequest')
    Unauthorized = (401, 'Unauthorized')
    Forbidden = (403, 'Forbidden')
    NotFound = (404, 'NotFound')
    NotAcceptable = (406, 'NotAcceptable')
    Conflict = (409, 'Conflict')
    InternalServerError = (500, 'InternalServerError')


class Standard(enum.Enum):
    NonAuthoritativeInformation = (203, 'NonAuthoritativeInformation')
    ResetContent = (205, 'ResetContent')
    PartialContent = (206, 'PartialContent')
    MultiStatus = (207, 'MultiStatus')
    AlreadyReported = (208, 'AlreadyReported')
    IMUsed = (226, 'IMUsed')
    MultipleChoices = (300, 'MultipleChoices')
    MovedPermanently = (301, 'MovedPermanently')
    Found = (302, 'Found')
    SeeOther = (303, 'SeeOther')
    NotModified = (304, 'NotModified')
    UseProxy = (305, 'UseProxy')
    SwitchProxy = (306, 'SwitchProxy')
    TemporaryRedirect = (307, 'TemporaryRedirect')
    PermanentRedirect = (308, 'PermanentRedirect')
    PaymentRequired = (402, 'PaymentRequired')
    MethodNotAllowed = (405, 'MethodNotAllowed')
    ProxyAuthenticationRequired = (407, 'ProxyAuthenticationRequired')
    RequestTimeout = (408, 'RequestTimeout')
    Gone = (410, 'Gone')
    LengthRequired = (411, 'LengthRequired')
    PreconditionFailed = (412, 'PreconditionFailed')
    PayloadTooLarge = (413, 'PayloadTooLarge')
    URITooLong = (414, 'URITooLong')
    UnsupportedMediaType = (415, 'UnsupportedMediaType')
    RangeNotSatisfiable = (416, 'RangeNotSatisfiable')
    ExpectationFailed = (417, 'ExpectationFailed')
    ImATeapot = (418, 'ImATeapot')
    MisdirectedRequest = (421, 'MisdirectedRequest')
    UnprocessableEntity = (422, 'UnprocessableEntity')
    Locked = (423, 'Locked')
    FailedDependency = (424, 'FailedDependency')
    TooEarly = (425, 'TooEarly')
    UpgradeRequired = (426, 'UpgradeRequired')
    PreconditionRequired = (428, 'PreconditionRequired')
    TooManyRequests = (429, 'TooManyRequests')
    RequestHeaderFieldsTooLarge = (431, 'RequestHeaderFieldsTooLarge')
    UnavailableForLegalReasons = (451, 'UnavailableForLegalReasons')
    NotImplemented = (501, 'NotImplemented')
    ServiceUnavailable = (503, 'ServiceUnavailable')
    GatewayTimeout = (504, 'GatewayTimeout')
    HTTPVersionNotSupported = (505, 'HTTPVersionNotSupported')
    VariantAlsoNegotiates = (506, 'VariantAlsoNegotiates')
    InsufficientStorage = (507, 'InsufficientStorage')
    LoopDetected = (508, 'LoopDetected')
    NotExtended = (510, 'NotExtended')
    NetworkAuthenticationRequired = (511, 'NetworkAuthenticationRequired')


class Extended(enum.Enum):
    ThisIsFine = (218, 'ThisIsFine')
    PageExpired = (419, 'PageExpired')
    EnhanceYourCalm = (420, 'EnhanceYourCalm')
    ShopifyRequestHeaderFieldsTooLarge = (430, 'ShopifyRequestHeaderFieldsTooLarge')
    BlockedbyWindowsParentalControls = (450, 'BlockedbyWindowsParentalControls')
    InvalidToken = (498, 'InvalidToken')
    BandwidthLimitExceeded = (509, 'BandwidthLimitExceeded')
    InvalidSSLCertificate = (526, 'InvalidSSLCertificate')
    SiteIsoverloaded = (529, 'SiteIsoverloaded')
    Networkreadtimeouterror = (598, 'Networkreadtimeouterror')
    IISLoginTimeOut = (440, 'IISLoginTimeOut')
    IISRetryWith = (449, 'IISRetryWith')
    NginxNoResponse = (444, 'NginxNoResponse')
    NginxRequestheadertoolarge = (494, 'NginxRequestheadertoolarge')
    NginxSSLCertificateError = (495, 'NginxSSLCertificateError')
    NginxSSLCertificateRequired = (496, 'NginxSSLCertificateRequired')
    NginxHTTPRequestSenttoHTTPSPort = (497, 'NginxHTTPRequestSenttoHTTPSPort')
    NginxClientClosedRequest = (499, 'NginxClientClosedRequest')
    CloudflareWebServerReturnedanUnknownError = (520, 'CloudflareWebServerReturnedanUnknownError')
    CloudflareWebServerIsDown = (521, 'CloudflareWebServerIsDown')
    CloudflareConnectionTimedOut = (522, 'CloudflareConnectionTimedOut')
    CloudflareOriginIsUnreachable = (523, 'CloudflareOriginIsUnreachable')
    CloudflareATimeoutOccurred = (524, 'CloudflareATimeoutOccurred')
    CloudflareSSLHandshakeFailed = (525, 'CloudflareSSLHandshakeFailed')
    CloudflareRailgunError = (527, 'CloudflareRailgunError')
    CloudflareThousandError = (530, 'CloudflareThousandError')
    AWSClientClosed = (460, 'AWSClientClosed')
    AWSTooManyIps = (463, 'AWSTooManyIps')
